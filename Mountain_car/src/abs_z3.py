import pandas as pd
import sys
import time
from z3 import *
import argparse

import numpy as np

sys.setrecursionlimit(1000)

def over_func(df):
    distances = np.sqrt((df['pos'].values[:, np.newaxis] - df['pos'].values) ** 2 +
                        (df['vel'].values[:, np.newaxis] - df['vel'].values) ** 2)

    
    mask = (distances < 10) & (df['result'].values[:, np.newaxis] == df['result'].values) & \
        (df['network'].values[:, np.newaxis] == df['network'].values)

    
    merged_df = df[mask.any(axis=1)].drop_duplicates(subset=['network', 'result'])
    merged_df = pd.concat([df, merged_df], ignore_index=True)
    return merged_df



def MMC1_z3(df,dataorginal):
    df2 = df.loc[df['result'] == False]
    

    t1 = time.time()


    for index, row in df2.iterrows():
        pos_value = row['pos']
        vel_value = row['vel']
        network_value = row['network']
        fix_value = [pos_value,vel_value,network_value]
        
        network_var = String('network')
        pos_var = Real('pos')
        vel_var = Real('vel')
        result_var = Bool('result')
        counterexmaple1 = dataorginal
        counterexmaple2 = dataorginal
        counterexmaple3 = dataorginal


        solver = Solver()


        network_constraint = network_var != row['network']
        pos_constraint = pos_var == row['pos']
        vel_constraint = vel_var == row['vel']
        result_constraint = result_var == True

        
        solver.add(network_constraint)
        solver.add(pos_constraint)
        solver.add(vel_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            network_value = model.eval(network_var).as_string()
            pos_value = float(model.eval(pos_var).numerator_as_long()) / float(model.eval(pos_var).denominator_as_long())
            vel_value = float(model.eval(vel_var).numerator_as_long()) / float(model.eval(vel_var).denominator_as_long())

            result_row = df.loc[(df['network'] != row['network']) & (df['pos'] == row['pos']) & (df['vel'] == row['vel']) & (df['result'] == True)]
            if len(result_row) > 0:
                
                cause = network_value
                var = 'network'
                return True ,cause , var, fix_value
            else:
                counterexmaple1 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['vel'] == vel_value) & (dataorginal['pos'] == pos_value) & (dataorginal['network'] != network_value)]
        
        network_var = String('network')
        pos_var = Real('pos')
        vel_var = Real('vel')
        result_var = Bool('result')


        solver = Solver()


        network_constraint = network_var == row['network']
        pos_constraint = pos_var != row['pos']
        vel_constraint = vel_var == row['vel']
        result_constraint = result_var == True

        
        solver.add(network_constraint)
        solver.add(pos_constraint)
        solver.add(vel_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            network_value = model.eval(network_var).as_string()
            pos_value = float(model.eval(pos_var).numerator_as_long()) / float(model.eval(pos_var).denominator_as_long())
            vel_value = float(model.eval(vel_var).numerator_as_long()) / float(model.eval(vel_var).denominator_as_long())
            

            result_row = df.loc[(df['network'] == row['network']) & (df['pos'] != row['pos']) & (df['vel'] == row['vel']) & (df['result'] == True)]
            if len(result_row) > 0:
                
                cause = vel_value
                var = 'pos'
                return True ,cause , var, fix_value
            else:
                counterexmaple2 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['vel'] == vel_value) & (dataorginal['pos'] != pos_value) & (dataorginal['network'] == network_value)]
        

        network_var = String('network')
        pos_var = Real('pos')
        vel_var = Real('vel')
        result_var = Bool('result')


        solver = Solver()


        network_constraint = network_var == row['network']
        pos_constraint = pos_var == row['pos']
        vel_constraint = vel_var != row['vel']
        result_constraint = result_var == True

        
        solver.add(network_constraint)
        solver.add(pos_constraint)
        solver.add(vel_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            network_value = model.eval(network_var).as_string()
            pos_value = float(model.eval(pos_var).numerator_as_long()) / float(model.eval(pos_var).denominator_as_long())
            vel_value = float(model.eval(vel_var).numerator_as_long()) / float(model.eval(vel_var).denominator_as_long())
            

            result_row = df.loc[(df['network'] == row['network']) & (df['pos'] == row['pos']) & (df['vel'] != row['vel']) & (df['result'] == True)]
            if len(result_row) > 0:
                
                cause = pos_value
                var = 'vel'
                return True , cause , var, fix_value
            else:
                counterexmaple3 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['vel'] != vel_value) & (dataorginal['pos'] == pos_value) & (dataorginal['network'] == network_value)]
    
    counterexample = min(counterexmaple1,counterexmaple2,counterexmaple3,key=len)
    return False , counterexample , None, fix_value


def MMC2_z3(dataorginal,var,cause,fix_value):
    df = dataorginal
    pos_value = fix_value[0]
    vel_value = fix_value[1]
    network_value = fix_value[2]


    if var == 'network':
        network_var = String('network')
        pos_var = Real('pos')
        vel_var = Real('vel')
        result_var = Bool('result')


        solver = Solver()


        network_constraint = network_var == network_value
        pos_constraint = pos_var != pos_value
        vel_constraint = vel_var != vel_value
        result_constraint = result_var == False

        
        solver.add(network_constraint)
        solver.add(pos_constraint)
        solver.add(vel_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            network_value = model.eval(network_var).as_string()
            pos_value = float(model.eval(pos_var).numerator_as_long()) / float(model.eval(pos_var).denominator_as_long())
            vel_value = float(model.eval(vel_var).numerator_as_long()) / float(model.eval(vel_var).denominator_as_long())
            

            result_row = df.loc[(df['network'] == network_value) & (df['pos'] != pos_value) & (df['vel'] != vel_value) & (df['result'] == False)]
            if len(result_row) > 0:
                return True
            else:
                return False

    elif var == 'pos':
        network_var = String('network')
        pos_var = Real('pos')
        vel_var = Real('vel')
        result_var = Bool('result')


        solver = Solver()


        network_constraint = network_var != network_value
        pos_constraint = pos_var == pos_value
        vel_constraint = vel_var != vel_value
        result_constraint = result_var == False

       
        solver.add(network_constraint)
        solver.add(pos_constraint)
        solver.add(vel_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            network_value = model.eval(network_var).as_string()
            pos_value = float(model.eval(pos_var).numerator_as_long()) / float(model.eval(pos_var).denominator_as_long())
            vel_value = float(model.eval(vel_var).numerator_as_long()) / float(model.eval(vel_var).denominator_as_long())
            

            result_row = df.loc[(df['network'] == network_value) & (df['pos'] != pos_value) & (df['vel'] != vel_value) & (df['result'] == False)]
            if len(result_row) > 0:
                return True
            else:
                return False

    else:
        network_var = String('network')
        pos_var = Real('pos')
        vel_var = Real('vel')
        result_var = Bool('result')


        solver = Solver()


        network_constraint = network_var != network_value
        pos_constraint = pos_var != pos_value
        vel_constraint = vel_var == vel_value
        result_constraint = result_var == False

        
        solver.add(network_constraint)
        solver.add(pos_constraint)
        solver.add(vel_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            network_value = model.eval(network_var).as_string()
            pos_value = float(model.eval(pos_var).numerator_as_long()) / float(model.eval(pos_var).denominator_as_long())
            vel_value = float(model.eval(vel_var).numerator_as_long()) / float(model.eval(vel_var).denominator_as_long())
            

            result_row = df.loc[(df['network'] != network_value) & (df['pos'] != pos_value) & (df['vel'] == vel_value) & (df['result'] == False)]
            if len(result_row) > 0:
                return True
            else:
                return False


    
def under_approx(df,parm,refie_c):
    while True:
        refie_c = refie_c + 1

        data = df[0:parm]
        res, cause_or_counter,var,fix_value = MMC1_z3(data,df)
        if res == True:
            return data , cause_or_counter , refie_c , var , fix_value
        else:
            parm = int(parm*1.1)
            continue
    
            


def over_approx(causet,datat,dft,ref_c,var,fix_value):
    ref_c = ref_c+1
    dft1 = over_func(dft)
    res = MMC2_z3(dft,var,causet,fix_value)
    if res == True:
        return True , causet, ref_c, fix_value
    else:
        return False, causet, ref_c, fix_value 
    
def algo(dft,paramet):
    datat , causet, ref_c ,var, fix_value1 =  under_approx(dft,paramet,0)
    
    res, c, ref_c, fix_value1 = over_approx(causet,datat,dft,ref_c,var,fix_value1)
    if res==True:
        return causet, ref_c, fix_value1
    else:
        return algo(dft,paramet)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--init_parm", help="param", default=0.001)
    
    parser.add_argument("--init_trace", help="set of traces", default=100)
    args = parser.parse_args()

    
    init_parm = float(args.init_parm)
    init_trace = int(args.init_trace)
 
    
    dft = pd.read_csv('network_data.csv')
    dft = dft.sample(frac=1).reset_index(drop=True)

    dft = dft.iloc[0:init_trace]
    

    
    
    alpha = init_parm
    
    t1 = time.time()
    paramet = int(len(dft)*alpha)
    c, ref_c, fix_value1 = algo(dft,paramet)
    t2 = time.time()
    print("In set of trace pos :"+str(fix_value1[0])+"; vel: "+str(fix_value1[1])+"; network: "+str(fix_value1[2])+" cause is "+str(c), " with number of refienmnets "+ str(ref_c))
    print('time',(t2-t1)*1000)
