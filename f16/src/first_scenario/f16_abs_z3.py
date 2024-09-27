import pandas as pd
import sys
import time
from z3 import *
import argparse
import numpy as np
import time 

sys.setrecursionlimit(1000)

def over_func(df):
       distances = np.sqrt((df['altitude'].values[:, np.newaxis] - df['altitude'].values) ** 2 +
                     (df['speed'].values[:, np.newaxis] - df['speed'].values) ** 2)


       mask = (distances < 0.01) & (df['result'].values[:, np.newaxis] == df['result'].values) & \
              (df['power'].values[:, np.newaxis] == df['power'].values) & \
              (df['pit'].values[:, np.newaxis] == df['pit'].values)


       merged_df = df[mask.any(axis=1)].drop_duplicates(subset=['power', 'pit', 'result'])

       return merged_df


def MMC1_z3(df,dataorginal):
    df2 = df.loc[df['result'] == False]

    counterexmaple1 = dataorginal
    counterexmaple2 = dataorginal
    counterexmaple3 = dataorginal
    counterexmaple4 = dataorginal
    fix_value = []

    for index, row in df2.iterrows():
        
        altitude_value = row['altitude']
        pit_value = row['speed']
        power_value = row['power']
        pit_value = row['pit']
        fix_value = [altitude_value,pit_value,power_value,pit_value]
        
        power_var = Real('power')
        altitude_var = Real('altitude')
        pit_var = Real('speed')
        result_var = Bool('result')
        pit_var = Real('pit')
        


        solver = Solver()


        power_constraint = power_var != row['power']
        altitude_constraint = altitude_var == row['altitude']
        pit_constraint = pit_var == row['speed']
        pit_constraint = pit_var == row['pit']

        result_constraint = result_var == True

        
        solver.add(power_constraint)
        solver.add(altitude_constraint)
        solver.add(pit_constraint)
        solver.add(pit_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            

            result_row = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] == pit_value ) & (df['power'] != power_value) & (df['pit'] == pit_value)]

            if len(result_row) > 0:
                
                cause = power_value
                var = 'power'
                return True ,cause , var, fix_value
            else:
                counterexmaple1 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['altitude'] == altitude_value) & (dataorginal['speed'] == pit_value) & (dataorginal['power'] != power_value) & (df['pit'] == pit_value)]
        






        power_var = Real('power')
        altitude_var = Real('altitude')
        pit_var = Real('speed')
        result_var = Bool('result')
        pit_var = Real('pit')



        solver = Solver()


        power_constraint = power_var == row['power']
        altitude_constraint = altitude_var != row['altitude']
        pit_constraint = pit_var == row['speed']
        pit_constraint = pit_var == row['pit']

        result_constraint = result_var == True

        
        solver.add(power_constraint)
        solver.add(altitude_constraint)
        solver.add(pit_constraint)
        solver.add(pit_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
        

            result_row = df.loc[(df['result'] == True) & (df['altitude'] != altitude_value) & (df['speed'] == pit_value ) & (df['power'] == power_value) & (df['pit'] == pit_value)]

            if len(result_row) > 0:
                # print('yes')
                cause = altitude_value
                var = 'altitude'
                return True ,cause , var, fix_value
            else:
                counterexmaple2 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['altitude'] != altitude_value) & (dataorginal['speed'] == pit_value) & (dataorginal['power'] == power_value) & (df['pit'] == pit_value)]


        power_var = Real('power')
        altitude_var = Real('altitude')
        pit_var = Real('speed')
        result_var = Bool('result')
        pit_var = Real('pit')
        


        solver = Solver()


        power_constraint = power_var == row['power']
        altitude_constraint = altitude_var == row['altitude']
        pit_constraint = pit_var != row['speed']
        pit_constraint = pit_var == row['pit']

        result_constraint = result_var == True

        # Add constraints to the solver
        solver.add(power_constraint)
        solver.add(altitude_constraint)
        solver.add(pit_constraint)
        solver.add(pit_constraint)
        solver.add(result_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] != pit_value ) & (df['power'] == power_value) & (df['pit'] == pit_value)]

            if len(result_row) > 0:
                cause = pit_value
                var = 'speed'
                return True ,cause , var, fix_value
            else:
                counterexmaple3 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['altitude'] == altitude_value) & (dataorginal['speed'] != pit_value) & (dataorginal['power'] == power_value) & (df['pit'] == pit_value)]









        power_var = Real('power')
        altitude_var = Real('altitude')
        pit_var = Real('speed')
        result_var = Bool('result')
        pit_var = Real('pit')
        


        solver = Solver()


        power_constraint = power_var == row['power']
        altitude_constraint = altitude_var == row['altitude']
        pit_constraint = pit_var == row['speed']
        pit_constraint = pit_var != row['pit']

        result_constraint = result_var == True

        # Add constraints to the solver
        solver.add(power_constraint)
        solver.add(altitude_constraint)
        solver.add(pit_constraint)
        solver.add(pit_constraint)
        solver.add(result_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()
            

            result_row = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] == pit_value ) & (df['power'] == power_value) & (df['pit'] != pit_value)]

            if len(result_row) > 0:
                cause = pit_value
                var = 'altitude'
                return True ,cause , var, fix_value
            else:
                counterexmaple4 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['altitude'] == altitude_value) & (dataorginal['speed'] == pit_value) & (dataorginal['power'] == power_value) & (df['pit'] != pit_value)]



    counterexample = min(counterexmaple1,counterexmaple2,counterexmaple3,counterexmaple4,key=len)
    return False , counterexample , None, fix_value


def MMC2_z3(dataorginal,var,cause,fix_value):

    altitude_value = fix_value[0]
    pit_value  = fix_value[1]
    power_value = fix_value[2]
    pit_value = fix_value[3]
    df = dataorginal

    


    if var == 'power':
        power_var = Real('power')
        altitude_var = Real('altitude')
        pit_var = Real('speed')
        result_var = Bool('result')
        pit_var = Real('pit')


        solver = Solver()
        power_constraint = power_var == power_value
        altitude_constraint = altitude_var != altitude_value
        pit_constraint = pit_var != pit_value
        pit_constraint = pit_var != pit_value 

        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(power_constraint)
        solver.add(altitude_constraint)
        solver.add(pit_constraint)
        solver.add(result_constraint)
        solver.add(pit_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['altitude'] != altitude_value) & (df['speed'] != pit_value ) & (df['power'] == power_value) & (df['pit'] != pit_value)]

            if len(result_row) > 0:
                return True
            else:
                return False

    elif var == 'altitude':
        power_var = Real('power')
        altitude_var = Real('altitude')
        pit_var = Real('speed')
        result_var = Bool('result')
        pit_var = Real('pit')


        solver = Solver()
        power_constraint = power_var != power_value
        altitude_constraint = altitude_var == altitude_value
        pit_constraint = pit_var != pit_value
        pit_constraint = pit_var != pit_value 

        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(power_constraint)
        solver.add(altitude_constraint)
        solver.add(pit_constraint)
        solver.add(result_constraint)
        solver.add(pit_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['altitude'] == altitude_value) & (df['speed'] != pit_value ) & (df['power'] != power_value) & (df['pit'] != pit_value)]

            if len(result_row) > 0:
                return True
            else:
                return False

    elif var == 'speed':
        power_var = Real('power')
        altitude_var = Real('altitude')
        pit_var = Real('speed')
        result_var = Bool('result')
        pit_var = Real('pit')


        solver = Solver()
        power_constraint = power_var != power_value
        altitude_constraint = altitude_var != altitude_value
        pit_constraint = pit_var == pit_value
        pit_constraint = pit_var != pit_value 

        result_constraint = result_var == False

        
        solver.add(power_constraint)
        solver.add(altitude_constraint)
        solver.add(pit_constraint)
        solver.add(result_constraint)
        solver.add(pit_constraint)

        
        if solver.check() == sat:
            model = solver.model()
        

            result_row = df.loc[(df['result'] == False) & (df['altitude'] != altitude_value) & (df['speed'] == pit_value ) & (df['power'] != power_value) & (df['pit'] != pit_value)]

            if len(result_row) > 0:
                return True
            else:
                return False
    else:

        power_var = Real('power')
        altitude_var = Real('altitude')
        pit_var = Real('speed')
        result_var = Bool('result')
        pit_var = Real('pit')


        solver = Solver()
        power_constraint = power_var != power_value
        altitude_constraint = altitude_var != altitude_value
        pit_constraint = pit_var != pit_value
        pit_constraint = pit_var == pit_value 

        result_constraint = result_var == False

        
        solver.add(power_constraint)
        solver.add(altitude_constraint)
        solver.add(pit_constraint)
        solver.add(result_constraint)
        solver.add(pit_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            

            result_row = df.loc[(df['result'] == False) & (df['altitude'] != altitude_value) & (df['speed'] != pit_value ) & (df['power'] != power_value) & (df['pit'] == pit_value)]

            if len(result_row) > 0:
                return True
            else:
                return False



    
def under_approx(df,parm,refie_c):
    while True:
        refie_c = refie_c + 1
        data = df[0:int(parm)]
        
        res, cause_or_counter,var,fix_value = MMC1_z3(data,df)
        if res == True or res == False:
            return data , cause_or_counter , refie_c , var , fix_value
        else:
            parm = int(parm*1.2)
            continue
    

def over_approx(causet,datat,dft,ref_c,var,fix_value):
    ref_c = ref_c+1
    dft = over_func(dft)
    res = MMC2_z3(dft,var,causet,fix_value)
    if res == True:
        return True , causet, ref_c, fix_value
    else:
        return False, causet, ref_c, fix_value 
    
def algo(dft,paramet):
    datat , causet, ref_c ,var1, fix_value1 =  under_approx(dft,paramet,0)
    res, c, ref_c, fix_value1 = over_approx(causet,datat,dft,ref_c,var1,fix_value1)
    if res==True:
        return causet, ref_c, fix_value1
    else:
        return algo(dft,paramet*1.5)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--init_parm", help="param", default=0.5)
    parser.add_argument("--init_trace", help="set of traces", default=2000)
    args = parser.parse_args()

    
    init_parm = float(args.init_parm)
    init_trace = int(args.init_trace)
 
    
    alpha = init_parm

    dft = pd.read_csv('sc1_data.csv')
    # dft = dft.sample(frac=1).reset_index(drop=True)
    dft = dft.iloc[0:init_trace]

    t1 = time.time()
    paramet = int(len(dft)*alpha)
    c, ref_c, fix_value1 = algo(dft,paramet)
    t2 = time.time()
    print("In set of trace altitude :"+str(fix_value1[0])+"; speed: "+str(fix_value1[1])+"; power: "+str(fix_value1[2])+"; pit: "+str(fix_value1[3])+" cause is "+str(c), " with number of refienmnets "+ str(ref_c))
    print("time", (t2-t1)*1000)












