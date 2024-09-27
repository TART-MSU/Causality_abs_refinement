'''
Stanley Bak
Python version of GCAS maneuver benchmark
'''

from math import pi
from numpy import deg2rad

from RunF16Sim import RunF16Sim
from PassFailAutomaton import FlightLimitsPFA, FlightLimits
from CtrlLimits import CtrlLimits
from LowLevelController import LowLevelController
from Autopilot import GcasAutopilot
from controlledF16 import controlledF16

import time

import pandas as pd

#roll
#low airspeed
#aoa
#pitch
#sleep slope
#power

def print_progress_bar(percentage):
    bar_length = 50  # Length of the progress bar
    filled_length = int(bar_length * percentage // 100)
    bar = '|' * filled_length + ' ' * (bar_length - filled_length)
    print(f'\n \rProgress: [{bar}] {percentage:.1f}% \n', end='')

if __name__ == '__main__':

    data = []

    counter = 1

    c_p = 1
    c_f = 1

    all = 23040

    t1 = time.time()

    for v in range(300,350,10):
        for p in range(0,100,25):
            for r in range(-30,30,15):
                for pit in range(-40,40,10):
                    for aoa in range(-10,50,5):
                        for b in range(0,30,10):

                            t2=time.time()

                            t = t2 - t1
                            ts = (((all-counter)*t)/counter)/50



                            counter = counter + 1


                            print_progress_bar((counter/all)*100)


                            print('\nEstimated time: {} minute\n'.format(ts))

                            rate = ((c_p)/(c_p+c_f))*100


                            print('\n Proportion True to all: {} \n'.format(rate))

                            


                            

                            try:


                                flightLimits = FlightLimits()
                                ctrlLimits = CtrlLimits()
                                llc = LowLevelController(ctrlLimits)
                                ap = GcasAutopilot(llc.xequil, llc.uequil, flightLimits, ctrlLimits)
                                pass_fail = FlightLimitsPFA(flightLimits)
                                pass_fail.break_on_error = False

                                ### Initial Conditions ###
                                power = p # Power

                                # Default alpha & beta
                                alpha = deg2rad(aoa)# Trim Angle of Attack (rad)
                                beta = deg2rad(b)              # Side slip angle (rad)

                                # Initial Attitude
                                alt = 500
                                Vt = v                  # Pass at Vtg = 540;    Fail at Vtg = 550;
                                phi = deg2rad(r)        # Roll angle from wings level (rad)
                                theta = deg2rad(pit)    # Pitch angle from nose level (rad)
                                psi = deg2rad(0)             # Yaw angle from North (rad)

                                # Build Initial Condition Vectors
                                # state = [VT, alpha, beta, phi, theta, psi, P, Q, R, pn, pe, h, pow]
                                initialState = [Vt, alpha, beta, phi, theta, psi, 0, 0, 0, 0, 0, alt, power]

                                # if not None will do animation. Try a filename ending in .gif or .mp4 (slow). Using '' will plot to the screen.
                                animFilename = ''

                                # Select Desired F-16 Plant
                                f16_plant = 'morelli' # 'stevens' or 'morelli'

                                tMax = 15 # simulation time

                                xcg_mult = 1.0 # center of gravity multiplier

                                val = 1.0      # other aerodynmic coefficient multipliers
                                cxt_mult = val
                                cyt_mult = val
                                czt_mult = val
                                clt_mult = val
                                cmt_mult = val
                                cnt_mult = val

                                multipliers = (xcg_mult, cxt_mult, cyt_mult, czt_mult, clt_mult, cmt_mult, cnt_mult)

                                der_func = lambda t, y: controlledF16(t, y, f16_plant, ap, llc, multipliers=multipliers)[0]

                                passed, times, states, modes, ps_list, Nz_list, u_list = RunF16Sim(initialState, tMax, der_func, f16_plant, ap, llc, pass_fail, multipliers=multipliers)

                                data.append([v,p,r,pit,aoa,b,passed])

                                print(v,p,r,pit,aoa,b,passed)

                                if passed ==True:
                                    c_p = c_p +1
                                else:
                                    c_f = c_f +1
                                

                                
                            except Exception as e:
                                print(e)
                                continue
    # print(len(listi))
    # print(listi)

    column_names = ["speed","power","roll","pitch","aoa",'slip',"result"]

    df = pd.DataFrame(data, columns=column_names)

    df.to_csv('sc2_data.csv', index=False)

        
