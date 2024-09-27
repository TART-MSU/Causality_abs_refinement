import pandas as pd
import sys
import time
from z3 import *
import argparse
import numpy as np
import time 

sys.setrecursionlimit(1000)

def over_func(df):
       distances = np.sqrt((df['aoa'].values[:, np.newaxis] - df['aoa'].values) ** 2 +
                     (df['slip'].values[:, np.newaxis] - df['slip'].values) ** 2 +
                     (df['pit'].values[:, np.newaxis] - df['pit'].values) ** 2+
                      (df['roll'].values[:, np.newaxis] - df['roll'].values) ** 2)


       mask = (distances < 100) & (df['result'].values[:, np.newaxis] == df['result'].values) & \
              (df['speed'].values[:, np.newaxis] == df['speed'].values) & \
              (df['power'].values[:, np.newaxis] == df['power'].values)


       merged_df = df[mask.any(axis=1)].drop_duplicates(subset=['power', 'pit', 'result'])

       return merged_df


def MMC1_z3(df,dataorginal):
    df2 = df.loc[df['result'] == False]

    counterexmaple1 = dataorginal
    counterexmaple2 = dataorginal
    counterexmaple3 = dataorginal
    counterexmaple4 = dataorginal
    counterexmaple5 = dataorginal
    counterexmaple6 = dataorginal

    for index, row in df2.iterrows():
        
        roll_value = row['roll']
        speed_value = row['speed']
        power_value = row['power']
        pit_value = row['pit']
        aoa_value = row['aoa']
        slip_value = row['slip']
        fix_value = [roll_value,speed_value,power_value,pit_value,aoa_value,slip_value]
        
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
            

            result_row = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] != pit_value) & (df['aoa'] == aoa_value) & (df['slip'] == slip_value) ]


            if len(result_row) > 0:
                
                cause = power_value
                var = 'pit'
                return True ,cause , var, fix_value
            else:
                counterexmaple1 = dataorginal.loc[(df['result'] == True) & (dataorginal['roll'] == roll_value) & (dataorginal['speed'] == speed_value ) & (dataorginal['power'] == power_value) & (dataorginal['pit'] != pit_value) & (dataorginal['aoa'] == aoa_value) & (dataorginal['slip'] == slip_value) ]
        
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
            

            result_row = df.loc[(df['result'] == True) & (df['roll'] != roll_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value) & (df['aoa'] == aoa_value) & (df['slip'] == slip_value) ]


            if len(result_row) > 0:
                
                cause = power_value
                var = 'roll'
                return True ,cause , var, fix_value
            else:
                counterexmaple2 = dataorginal.loc[(df['result'] == True) & (dataorginal['roll'] != roll_value) & (dataorginal['speed'] == speed_value ) & (dataorginal['power'] == power_value) & (dataorginal['pit'] == pit_value) & (dataorginal['aoa'] == aoa_value) & (dataorginal['slip'] == slip_value) ]
        


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
            

            result_row = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] != speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value) & (df['aoa'] == aoa_value) & (df['slip'] == slip_value) ]


            if len(result_row) > 0:
                
                cause = power_value
                var = 'speed'
                return True ,cause , var, fix_value
            else:
                counterexmaple3 = dataorginal.loc[(df['result'] == True) & (dataorginal['roll'] == roll_value) & (dataorginal['speed'] != speed_value ) & (dataorginal['power'] == power_value) & (dataorginal['pit'] == pit_value) & (dataorginal['aoa'] == aoa_value) & (dataorginal['slip'] == slip_value) ]
        

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
            

            result_row = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] == speed_value ) & (df['power'] != power_value) & (df['pit'] == pit_value) & (df['aoa'] == aoa_value) & (df['slip'] == slip_value) ]


            if len(result_row) > 0:
                
                cause = power_value
                var = 'power'
                return True ,cause , var, fix_value
            else:
                counterexmaple4 = dataorginal.loc[(df['result'] == True) & (dataorginal['roll'] == roll_value) & (dataorginal['speed'] == speed_value ) & (dataorginal['power'] != power_value) & (dataorginal['pit'] == pit_value) & (dataorginal['aoa'] == aoa_value) & (dataorginal['slip'] == slip_value) ]
        


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
            

            result_row = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value) & (df['aoa'] != aoa_value) & (df['slip'] == slip_value) ]


            if len(result_row) > 0:
                
                cause = power_value
                var = 'aoa'
                return True ,cause , var, fix_value
            else:
                counterexmaple5 = dataorginal.loc[(df['result'] == True) & (dataorginal['roll'] == roll_value) & (dataorginal['speed'] == speed_value ) & (dataorginal['power'] == power_value) & (dataorginal['pit'] == pit_value) & (dataorginal['aoa'] != aoa_value) & (dataorginal['slip'] == slip_value) ]
        


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
            

            result_row = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value) & (df['aoa'] == aoa_value) & (df['slip'] != slip_value) ]


            if len(result_row) > 0:
                
                cause = power_value
                var = 'slip'
                return True ,cause , var, fix_value
            else:
                counterexmaple6 = dataorginal.loc[(df['result'] == True) & (dataorginal['roll'] == roll_value) & (dataorginal['speed'] == speed_value ) & (dataorginal['power'] == power_value) & (dataorginal['pit'] == pit_value) & (dataorginal['aoa'] == aoa_value) & (dataorginal['slip'] != slip_value) ]
        
    

    counterexample = min(counterexmaple1,counterexmaple2,counterexmaple3,counterexmaple4,counterexmaple5,counterexmaple6,key=len)
    return False , counterexample , None, fix_value


def MMC2_z3(dataorginal,var,cause,fix_value):

    roll_value = fix_value[0]
    speed_value  = fix_value[1]
    power_value = fix_value[2]
    pit_value = fix_value[3]
    aoa_value = fix_value[4]
    slip_value = fix_value[5]
    df = dataorginal

    


    if var == 'pit':
        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()
        pit_constraint = pit_var == pit_value
        roll_constraint = roll_var != roll_value
        speed_constraint = speed_var != speed_value
        power_constraint = power_var != power_value
        aoa_constraint = aoa_var != aoa_value
        slip_constraint = slip_var != slip_value


        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['roll'] != roll_value) & (df['speed'] != speed_value ) & (df['power'] != power_value) & (df['pit'] == pit_value) & (df['aoa'] != aoa_value) & (df['slip'] != slip_value) ]


            if len(result_row) > 0:
                return True
            else:
                return False

    elif var == 'roll':

        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')
        


        solver = Solver()
        pit_constraint = pit_var != pit_value
        roll_constraint = roll_var == roll_value
        speed_constraint = speed_var != speed_value
        power_constraint = power_var != power_value
        aoa_constraint = aoa_var != aoa_value
        slip_constraint = slip_var != slip_value


        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['roll'] == roll_value) & (df['speed'] != speed_value ) & (df['power'] != power_value) & (df['pit'] != pit_value) & (df['aoa'] != aoa_value) & (df['slip'] != slip_value) ]


            if len(result_row) > 0:
                return True
            else:
                return False
            
    elif var == 'speed':
        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()
        
        pit_constraint = pit_var != pit_value
        roll_constraint = roll_var != roll_value
        speed_constraint = speed_var == speed_value
        power_constraint = power_var != power_value
        aoa_constraint = aoa_var != aoa_value
        slip_constraint = slip_var != slip_value


        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['roll'] != roll_value) & (df['speed'] == speed_value ) & (df['power'] != power_value) & (df['pit'] != pit_value) & (df['aoa'] != aoa_value) & (df['slip'] != slip_value) ]


            if len(result_row) > 0:
                return True
            else:
                return False
    
    elif var == 'power':
        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()
        pit_constraint = pit_var != pit_value
        roll_constraint = roll_var != roll_value
        speed_constraint = speed_var != speed_value
        power_constraint = power_var == power_value
        aoa_constraint = aoa_var != aoa_value
        slip_constraint = slip_var != slip_value


        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['roll'] == roll_value) & (df['speed'] != speed_value ) & (df['power'] == power_value) & (df['pit'] != pit_value) & (df['aoa'] != aoa_value) & (df['slip'] != slip_value) ]


            if len(result_row) > 0:
                return True
            else:
                return False
            
    elif var == 'aoa':
        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()
        pit_constraint = pit_var != pit_value
        roll_constraint = roll_var != roll_value
        speed_constraint = speed_var != speed_value
        power_constraint = power_var != power_value
        aoa_constraint = aoa_var == aoa_value
        slip_constraint = slip_var != slip_value


        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['roll'] == roll_value) & (df['speed'] != speed_value ) & (df['power'] != power_value) & (df['pit'] != pit_value) & (df['aoa'] == aoa_value) & (df['slip'] != slip_value) ]


            if len(result_row) > 0:
                return True
            else:
                return False

    
    else:

        pit_var = Real('pit')
        roll_var = Real('roll')
        speed_var = Real('speed')
        result_var = Bool('result')
        power_var = Real('power')
        aoa_var = Real('aoa')
        slip_var = Real('slip')


        solver = Solver()
        

        pit_constraint = pit_var != pit_value
        roll_constraint = roll_var != roll_value
        speed_constraint = speed_var != speed_value
        power_constraint = power_var != power_value
        aoa_constraint = aoa_var != aoa_value
        slip_constraint = slip_var == slip_value


        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(pit_constraint)
        solver.add(roll_constraint)
        solver.add(speed_constraint)
        solver.add(power_constraint)
        solver.add(result_constraint)
        solver.add(aoa_constraint)
        solver.add(slip_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['roll'] == roll_value) & (df['speed'] != speed_value ) & (df['power'] != power_value) & (df['pit'] != pit_value) & (df['aoa'] != aoa_value) & (df['slip'] == slip_value) ]


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
    if res == True or res==False:
        return True , causet, ref_c, fix_value
    else:
        return False, causet, ref_c, fix_value 
    
def algo(dft,paramet):
    datat , causet, ref_c ,var1, fix_value1 =  under_approx(dft,paramet,0)
    # print(causet)
    # print(causet,ref_c,var1,fix_value1)
    res, c, ref_c, fix_value1 = over_approx(causet,datat,dft,ref_c,var1,fix_value1)
    if res==True or res==False:
        return causet, ref_c, fix_value1
    else:
        return algo(dft,paramet*1.5)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--init_parm", help="param", default=0.1)
    parser.add_argument("--init_trace", help="set of traces", default=20000)
    args = parser.parse_args()

    
    init_parm = float(args.init_parm)
    init_trace = int(args.init_trace)
 
    
    alpha = init_parm

    dft = pd.read_csv('result_case2.csv')
    # dft = dft.sample(frac=1).reset_index(drop=True)
    dft = dft.iloc[0:init_trace]

    t1 = time.time()
    paramet = int(len(dft)*alpha)
    c, ref_c, fix_value1 = algo(dft,paramet)
    t2 = time.time()
    # print("In set of tarce roll :"+str(fix_value1[0])+"; speed: "+str(fix_value1[1])+"; power: "+str(fix_value1[2])+"; pit: "+str(fix_value1[3])+"; aoa: "+str(fix_value1[4])+"; slip: "+str(fix_value1[5])+" cause is "+str(c), " with number of refienmnets "+ str(ref_c))
    # print('time',(t2-t1)*1000)

