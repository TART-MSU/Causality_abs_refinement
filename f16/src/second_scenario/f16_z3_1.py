import pandas as pd
from z3 import *
import time  
import argparse


#speed,power,roll,pit,aoa,slip,result

def Algo_n_abs_z3(df):
    
    df2 = df.loc[df['result'] == False]
    # print(df2)
    f = open("result_z3_1.txt", "a")
    

    t1 = time.time()


    for index, row in df2.iterrows():
        
        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()

        pit_constraint = pit_var != row['pit']
        roll_constraint = roll_var == row['roll']
        speed_constraint = speed_var == row['speed']
        power_constraint = power_var == row['power']
        aoa_constraint = aoa_var == row['aoa']
        slip_constraint = slip_var == row['slip']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['roll'] == row['roll']) & (df['speed'] == row['speed'] ) & (df['pit'] != row['pit']) & (df['power'] == row['power']) & (df['aoa'] == row['aoa']) & (df['slip'] == row['slip'])]


            
            if len(result_row) > 0:
                f.write("Cause is pit : "+ str(row['pit'])+"\n")
                pass
        
        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()

        pit_constraint = pit_var == row['pit']
        roll_constraint = roll_var != row['roll']
        speed_constraint = speed_var == row['speed']
        power_constraint = power_var == row['power']
        aoa_constraint = aoa_var == row['aoa']
        slip_constraint = slip_var == row['slip']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['roll'] != row['roll']) & (df['speed'] == row['speed'] ) & (df['pit'] == row['pit']) & (df['power'] == row['power']) & (df['aoa'] == row['aoa']) & (df['slip'] == row['slip'])]


            
            if len(result_row) > 0:
                f.write("Cause is roll : "+ str(row['pit'])+"\n")
                pass
        

        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()

        pit_constraint = pit_var == row['pit']
        roll_constraint = roll_var == row['roll']
        speed_constraint = speed_var != row['speed']
        power_constraint = power_var == row['power']
        aoa_constraint = aoa_var == row['aoa']
        slip_constraint = slip_var == row['slip']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['roll'] == row['roll']) & (df['speed'] != row['speed'] ) & (df['pit'] == row['pit']) & (df['power'] == row['power']) & (df['aoa'] == row['aoa']) & (df['slip'] == row['slip'])]


            
            if len(result_row) > 0:
                f.write("Cause is speed : "+ str(row['pit'])+"\n")
                pass
        

        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()

        pit_constraint = pit_var == row['pit']
        roll_constraint = roll_var == row['roll']
        speed_constraint = speed_var == row['speed']
        power_constraint = power_var != row['power']
        aoa_constraint = aoa_var == row['aoa']
        slip_constraint = slip_var == row['slip']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['roll'] == row['roll']) & (df['speed'] == row['speed'] ) & (df['pit'] == row['pit']) & (df['power'] != row['power']) & (df['aoa'] == row['aoa']) & (df['slip'] == row['slip'])]


            
            if len(result_row) > 0:
                f.write("Cause is power : "+ str(row['pit'])+"\n")
                pass

        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()

        pit_constraint = pit_var == row['pit']
        roll_constraint = roll_var == row['roll']
        speed_constraint = speed_var == row['speed']
        power_constraint = power_var == row['power']
        aoa_constraint = aoa_var != row['aoa']
        slip_constraint = slip_var == row['slip']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['roll'] == row['roll']) & (df['speed'] == row['speed'] ) & (df['pit'] == row['pit']) & (df['power'] == row['power']) & (df['aoa'] != row['aoa']) & (df['slip'] == row['slip'])]


            
            if len(result_row) > 0:
                f.write("Cause is aoa : "+ str(row['pit'])+"\n")
                pass

        
        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()

        pit_constraint = pit_var == row['pit']
        roll_constraint = roll_var == row['roll']
        speed_constraint = speed_var == row['speed']
        power_constraint = power_var == row['power']
        aoa_constraint = aoa_var == row['aoa']
        slip_constraint = slip_var != row['slip']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['roll'] == row['roll']) & (df['speed'] == row['speed'] ) & (df['pit'] == row['pit']) & (df['power'] == row['power']) & (df['aoa'] == row['aoa']) & (df['slip'] != row['slip'])]


            
            if len(result_row) > 0:
                f.write("Cause is slip : "+ str(row['pit'])+"\n")
                pass
        



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    
    parser.add_argument("--init_trace", help="set of trace", default=20000)
    args = parser.parse_args()

    
    init_trace = int(args.init_trace)
    
 
    dft = pd.read_csv('result_case2.csv')



    dft = dft.iloc[0:init_trace]

    
    t1 = time.time()
    Algo_n_abs_z3(dft)
    t2 = time.time()
    # print('time:', (t2-t1)*1000)
    # print('Cause in traces saved in file result_z3_1.txt')