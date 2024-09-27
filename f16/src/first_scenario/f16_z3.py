import pandas as pd
from z3 import *
import time 
import argparse

def Algo_n_abs_z3(df):
    
    df2 = df.loc[df['result'] == False]
    # print(df2)
    f = open("result_z3.txt", "a")
    

    t1 = time.time()


    for index, row in df2.iterrows():
        
        pit_var = Real('pit')
        altitude_var = Real('altitude')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')


        solver = Solver()

        pit_constraint = pit_var != row['pit']
        altitude_constraint = altitude_var == row['altitude']
        speed_constraint = speed_var == row['speed']
        power_constraint = power_var == row['power']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(altitude_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['altitude'] == row['altitude']) & (df['speed'] == row['speed'] ) & (df['pit'] != row['pit']) & (df['power'] == row['power'])]


            
            if len(result_row) > 0:
                f.write("Cause is pit : "+ str(row['pit'])+"\n")
                pass
        
        pit_var = Real('pit')
        altitude_var = Real('altitude')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')


        solver = Solver()

        pit_constraint = pit_var == row['pit']
        altitude_constraint = altitude_var != row['altitude']
        speed_constraint = speed_var == row['speed']
        power_constraint = power_var == row['power']

        result_constraint = result_var == True


        # Add constraints to the solver
        solver.add(pit_constraint)
        solver.add(altitude_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
           
            model = solver.model()

            result_row1 = df.loc[(df['result'] == True) & (df['altitude'] != row['altitude']) & (df['speed'] == row['speed'] ) & (df['pit'] == row['pit']) & (df['power'] == row['power'])]


            
            if len(result_row1) > 0:
                f.write("Cause is altitude : "+ str(row['altitude'])+"\n")
                pass
        

        pit_var = Real('pit')
        altitude_var = Real('altitude')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')


        solver = Solver()

        pit_constraint = pit_var == row['pit']
        altitude_constraint = altitude_var == row['altitude']
        speed_constraint = speed_var != row['speed']
        power_constraint = power_var == row['power']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(altitude_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row2 = df.loc[(df['result'] == True) & (df['altitude'] == row['altitude']) & (df['speed'] != row['speed'] ) & (df['pit'] == row['pit']) & (df['power'] == row['power'])]


            
            if len(result_row2) > 0:
                f.write("Cause is speed : "+ str(row['speed'])+"\n")
                pass
        

        pit_var = Real('pit')
        altitude_var = Real('altitude')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')


        solver = Solver()

        pit_constraint = pit_var != row['pit']
        altitude_constraint = altitude_var == row['altitude']
        speed_constraint = speed_var == row['speed']
        power_constraint = power_var != row['power']

        result_constraint = result_var == True


        
        solver.add(pit_constraint)
        solver.add(altitude_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
        

            result_row3 = df.loc[(df['result'] == True) & (df['altitude'] == row['altitude']) & (df['speed'] == row['speed'] ) & (df['pit'] == row['pit']) & (df['power'] != row['power'])]


            
            if len(result_row3) > 0:
                f.write("Cause is power : "+ str(row['power'])+"\n")
                pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    
    parser.add_argument("--init_trace", help="set of trace", default=1000)
    args = parser.parse_args()

    
    init_trace = int(args.init_trace)
    
 
    dft = pd.read_csv('check_resut.csv')

    dft = dft.sample(frac=1).reset_index(drop=True)


    dft = dft.iloc[0:init_trace]

    
    t1 = time.time()
    Algo_n_abs_z3(dft)
    t2 = time.time()
    print('time:', (t2-t1)*1000)
    print('Cause in traces saved in file result_z3.txt')