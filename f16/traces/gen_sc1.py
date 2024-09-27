'''
Stanley Bak

Engine controller specification checking
'''

import numpy as np
from numpy import deg2rad
import pandas as pd

from RunF16Sim import RunF16Sim
from PassFailAutomaton import AirspeedPFA, FlightLimits
from CtrlLimits import CtrlLimits
from LowLevelController import LowLevelController
from Autopilot import FixedSpeedAutopilot
from controlledF16 import controlledF16

from PassFailAutomaton import FlightLimitsPFA, FlightLimits
from Autopilot import FixedAltitudeAutopilot
from plot import plot2d



if __name__ == '__main__':

    data = []

    setpoint_v = 800
    p_gain = 0.1

    setpoint_l = 5000 # altitude setpoint

    counter = 0
    for a in range(setpoint_l-500,setpoint_l+500,50):
        for v in range(300,setpoint_v,50):
            for p in range(0,30,5):
                for pit in range(-20,20,5):
                    counter = counter +1
                    try:

                        print(a,v,p,pit)
                        print(counter)

                        if pit > 10 and pit :
                            al = pit - 5
                        elif pit < 0:
                            al = pit + 5
                        else:
                            al = pit 

                        # print("alt :{}, speed:{}, power:{}".format(a,v,p))

                        ctrlLimits = CtrlLimits()
                        flightLimits = FlightLimits()
                        llc = LowLevelController(ctrlLimits)

                        

                        ap = FixedSpeedAutopilot(setpoint_v, p_gain, llc.xequil, llc.uequil, flightLimits, ctrlLimits)

                        pass_fail = AirspeedPFA(60, setpoint_v, 5)

                        ### Initial Conditions ###
                        power = p # Power

                        # Default alpha & beta
                        alpha = deg2rad(al) # Trim Angle of Attack (rad)
                        beta = 0                # Side slip angle (rad)

                        alt = a # Initial Attitude
                        Vt = v # Initial Speed
                        phi = 0 #(pi/2)*0.5           # Roll angle from wings level (rad)
                        theta = deg2rad(pit) #(-pi/2)*0.8        # Pitch angle from nose level (rad)
                        psi = 0 #-pi/4                # Yaw angle from North (rad)

                        # Build Initial Condition Vectors
                        # state = [VT, alpha, beta, phi, theta, psi, P, Q, R, pn, pe, h, pow]
                        initialState = [Vt, alpha, beta, phi, theta, psi, 0, 0, 0, 0, 0, alt, power]

                        # Select Desired F-16 Plant
                        f16_plant = 'morelli' # 'stevens' or 'morelli'

                        tMax = 60 # simulation time

                        def der_func(t, y):
                            'derivative function'

                            der = controlledF16(t, y, f16_plant, ap, llc)[0]

                            rv = np.zeros((y.shape[0],))

                            rv[0] = der[0] # speed
                            rv[12] = der[12] # power lag term

                            return rv

                        passed_e, times, states, modes, ps_list, Nz_list, u_list = RunF16Sim(initialState, tMax, der_func, f16_plant, ap, llc, pass_fail, sim_step=0.1)










                        ##############################################################################################
                        ##############################################################################################
                        ##############################################################################################
                        #########################altidude problem ###############################################
                        ##############################################################################################
                        ##############################################################################################
                        ##############################################################################################











                        ctrlLimits = CtrlLimits()
                        flightLimits = FlightLimits()
                        llc = LowLevelController(ctrlLimits)

                        
                        ap = FixedAltitudeAutopilot(setpoint_l, llc.xequil, llc.uequil, flightLimits, ctrlLimits)

                        pass_fail = FlightLimitsPFA(flightLimits)
                        pass_fail.break_on_error = False

                        ### Initial Conditions ###
                        power = p # Power

                        # Default alpha & beta
                        alpha = deg2rad(al) # angle of attack (rad)
                        beta = 0  # Side slip angle (rad)

                        alt = a # Initial Attitude
                        Vt = v # Initial Speed
                        phi = 0
                        theta = deg2rad(pit)
                        psi = 0

                        # Build Initial Condition Vectors
                        # state = [VT, alpha, beta, phi, theta, psi, P, Q, R, pn, pe, h, pow]
                        initialState = [Vt, alpha, beta, phi, theta, psi, 0, 0, 0, 0, 0, alt, power]

                        # Select Desired F-16 Plant
                        f16_plant = 'morelli' # 'stevens' or 'morelli'

                        tMax = 60 # simulation time

                        def der_func(t, y):
                            'derivative function for RK45'

                            der = controlledF16(t, y, f16_plant, ap, llc)[0]

                            rv = np.zeros((y.shape[0],))

                            rv[0] = der[0] # air speed
                            rv[1] = der[1] # alpha
                            rv[4] = der[4] # pitch angle
                            rv[7] = der[7] # pitch rate
                            rv[11] = der[11] # altitude
                            rv[12] = der[12] # power lag term
                            rv[13] = der[13] # Nz integrator

                            return rv

                        passed_l, times, states, modes, ps_list, Nz_list, u_list = RunF16Sim(initialState, tMax, der_func, f16_plant, ap, llc, pass_fail, sim_step=0.01)

                        # print ("Simulation Conditions Passed: {}".format(passed))

                        # plot
                        # filename = None # longitudinal.png
                        # plot2d(filename, times, [(states, [(0, 'Vt'), (11, 'Altitude')]), (u_list, [(0, 'Throttle'), (1, 'elevator')]), (Nz_list, [(0, 'Nz')]) ])




                        
                        


                        # print (passed)


                        # filename = None # engine_e.png
                        # plot2d(filename, times, [(states, [(0, 'Vt'), (12, 'Pow')]), (u_list, [(0, 'Throttle')])])

                        if passed_e == True and passed_l == True:
                            res = True
                        else:
                            res = False
                        data.append([a,v,p,pit,res])
                    except Exception as e:
                        print(e)
                        continue
    print(len(data))
    print(data)

    column_names = ["altitude","speed","power","pit",'result']

    df = pd.DataFrame(data, columns=column_names)

    df.to_csv('sc1_data.csv', index=False)

                
