import pandas as pd
import sys
import time
from z3 import *
import argparse
import numpy as np
import time 

sys.setrecursionlimit(1000)

def over_func(df):
       distances = np.sqrt((df['vel_x'].values[:, np.newaxis] - df['vel_x'].values) ** 2 +
                     (df['vel_y'].values[:, np.newaxis] - df['vel_y'].values) ** 2)


       mask = (distances < 0.01) & (df['result'].values[:, np.newaxis] == df['result'].values) & \
              (df['network'].values[:, np.newaxis] == df['network'].values) & \
              (df['wind'].values[:, np.newaxis] == df['wind'].values)


       merged_df = df[mask.any(axis=1)].drop_duplicates(subset=['network', 'wind', 'result'])

       return merged_df


def MMC1_z3(df,dataorginal):
    df2 = df.loc[df['result'] == False]
    # print(df2)
    # f = open("result_with_SMT_no_abstarct.txt", "a")
    # f1 = open("time.txt","a")

    t1 = time.time()
    counterexmaple1 = dataorginal
    counterexmaple2 = dataorginal
    counterexmaple3 = dataorginal
    counterexmaple4 = dataorginal
    fix_value = []

    for index, row in df2.iterrows():
        
        vel_x_value = row['vel_x']
        vel_y_value = row['vel_y']
        network_value = row['network']
        wind_value = row['wind']
        fix_value = [vel_x_value,vel_y_value,network_value,wind_value]
        
        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')
        


        solver = Solver()


        network_constraint = network_var != row['network']
        vel_x_constraint = vel_x_var == row['vel_x']
        vel_y_constraint = vel_y_var == row['vel_y']
        wind_constraint = wind_var == row['wind']

        result_constraint = result_var == True

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(vel_x_constraint)
        solver.add(vel_y_constraint)
        solver.add(wind_constraint)
        solver.add(result_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()
            

            result_row = df.loc[(df['result'] == True) & (df['vel_x'] == vel_x_value) & (df['vel_y'] == vel_y_value ) & (df['network'] != network_value) & (df['wind'] == wind_value)]

            if len(result_row) > 0:
                # print('yes')
                cause = network_value
                var = 'network'
                return True ,cause , var, fix_value
            else:
                counterexmaple1 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['vel_x'] == vel_x_value) & (dataorginal['vel_y'] == vel_y_value) & (dataorginal['network'] != network_value) & (df['wind'] == wind_value)]
        






        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')



        solver = Solver()


        network_constraint = network_var == row['network']
        vel_x_constraint = vel_x_var != row['vel_x']
        vel_y_constraint = vel_y_var == row['vel_y']
        wind_constraint = wind_var == row['wind']

        result_constraint = result_var == True

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(vel_x_constraint)
        solver.add(vel_y_constraint)
        solver.add(wind_constraint)
        solver.add(result_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()
        

            result_row = df.loc[(df['result'] == True) & (df['vel_x'] != vel_x_value) & (df['vel_y'] == vel_y_value ) & (df['network'] == network_value) & (df['wind'] == wind_value)]

            if len(result_row) > 0:
                # print('yes')
                cause = vel_x_value
                var = 'vel_x'
                return True ,cause , var, fix_value
            else:
                counterexmaple2 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['vel_x'] != vel_x_value) & (dataorginal['vel_y'] == vel_y_value) & (dataorginal['network'] == network_value) & (df['wind'] == wind_value)]
















        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')
        


        solver = Solver()


        network_constraint = network_var == row['network']
        vel_x_constraint = vel_x_var == row['vel_x']
        vel_y_constraint = vel_y_var != row['vel_y']
        wind_constraint = wind_var == row['wind']

        result_constraint = result_var == True

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(vel_x_constraint)
        solver.add(vel_y_constraint)
        solver.add(wind_constraint)
        solver.add(result_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == True) & (df['vel_x'] == vel_x_value) & (df['vel_y'] != vel_y_value ) & (df['network'] == network_value) & (df['wind'] == wind_value)]

            if len(result_row) > 0:
                # print('yes')
                cause = vel_y_value
                var = 'vel_y'
                return True ,cause , var, fix_value
            else:
                counterexmaple3 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['vel_x'] == vel_x_value) & (dataorginal['vel_y'] != vel_y_value) & (dataorginal['network'] == network_value) & (df['wind'] == wind_value)]









        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')
        


        solver = Solver()


        network_constraint = network_var == row['network']
        vel_x_constraint = vel_x_var == row['vel_x']
        vel_y_constraint = vel_y_var == row['vel_y']
        wind_constraint = wind_var != row['wind']

        result_constraint = result_var == True

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(vel_x_constraint)
        solver.add(vel_y_constraint)
        solver.add(wind_constraint)
        solver.add(result_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()
            

            result_row = df.loc[(df['result'] == True) & (df['vel_x'] == vel_x_value) & (df['vel_y'] == vel_y_value ) & (df['network'] == network_value) & (df['wind'] != wind_value)]

            if len(result_row) > 0:
                # print('yes')
                cause = wind_value
                var = 'vel_x'
                return True ,cause , var, fix_value
            else:
                counterexmaple4 = dataorginal.loc[(dataorginal['result'] == True) & (dataorginal['vel_x'] == vel_x_value) & (dataorginal['vel_y'] == vel_y_value) & (dataorginal['network'] == network_value) & (df['wind'] != wind_value)]



    counterexample = min(counterexmaple1,counterexmaple2,counterexmaple3,counterexmaple4,key=len)
    return False , counterexample , None, fix_value


def MMC2_z3(dataorginal,var,cause,fix_value):

    vel_x_value = fix_value[0]
    vel_y_value  = fix_value[1]
    network_value = fix_value[2]
    wind_value = fix_value[3]
    df = dataorginal

    


    if var == 'network':
        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')


        solver = Solver()
        network_constraint = network_var == network_value
        vel_x_constraint = vel_x_var != vel_x_value
        vel_y_constraint = vel_y_var != vel_y_value
        wind_constraint = wind_var != wind_value 

        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(vel_x_constraint)
        solver.add(vel_y_constraint)
        solver.add(result_constraint)
        solver.add(wind_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['vel_x'] != vel_x_value) & (df['vel_y'] != vel_y_value ) & (df['network'] == network_value) & (df['wind'] != wind_value)]

            if len(result_row) > 0:
                return True
            else:
                return False

    elif var == 'vel_x':
        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')


        solver = Solver()
        network_constraint = network_var != network_value
        vel_x_constraint = vel_x_var == vel_x_value
        vel_y_constraint = vel_y_var != vel_y_value
        wind_constraint = wind_var != wind_value 

        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(vel_x_constraint)
        solver.add(vel_y_constraint)
        solver.add(result_constraint)
        solver.add(wind_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()

            result_row = df.loc[(df['result'] == False) & (df['vel_x'] == vel_x_value) & (df['vel_y'] != vel_y_value ) & (df['network'] != network_value) & (df['wind'] != wind_value)]

            if len(result_row) > 0:
                return True
            else:
                return False

    elif var == 'vel_y':
        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')


        solver = Solver()
        network_constraint = network_var != network_value
        vel_x_constraint = vel_x_var != vel_x_value
        vel_y_constraint = vel_y_var == vel_y_value
        wind_constraint = wind_var != wind_value 

        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(vel_x_constraint)
        solver.add(vel_y_constraint)
        solver.add(result_constraint)
        solver.add(wind_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()
        

            result_row = df.loc[(df['result'] == False) & (df['vel_x'] != vel_x_value) & (df['vel_y'] == vel_y_value ) & (df['network'] != network_value) & (df['wind'] != wind_value)]

            if len(result_row) > 0:
                return True
            else:
                return False
    else:

        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')


        solver = Solver()
        network_constraint = network_var != network_value
        vel_x_constraint = vel_x_var != vel_x_value
        vel_y_constraint = vel_y_var != vel_y_value
        wind_constraint = wind_var == wind_value 

        result_constraint = result_var == False

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(vel_x_constraint)
        solver.add(vel_y_constraint)
        solver.add(result_constraint)
        solver.add(wind_constraint)

        # Check for satisfiability
        if solver.check() == sat:
            # Model is satisfiable, retrieve the values
            model = solver.model()
            

            result_row = df.loc[(df['result'] == False) & (df['vel_x'] != vel_x_value) & (df['vel_y'] != vel_y_value ) & (df['network'] != network_value) & (df['wind'] == wind_value)]

            if len(result_row) > 0:
                return True
            else:
                return False



    
def under_approx(df,parm,refie_c):
    while True:
        refie_c = refie_c + 1
        data = df[0:parm]
        # print(data)
        res, cause_or_counter,var,fix_value = MMC1_z3(data,df)
        if res == True:
            return data , cause_or_counter , refie_c , var , fix_value
        else:
            parm = int(parm*1.1)
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
    # print(causet)
    print(causet,ref_c,var1,fix_value1)
    res, c, ref_c, fix_value1 = over_approx(causet,datat,dft,ref_c,var1,fix_value1)
    if res==True:
        return causet, ref_c, fix_value1
    else:
        return algo(dft,paramet*1.5)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--init_parm", help="param", default=0.001)
    # parser.add_argument("--init_data", help="name of data", default="network_data.csv")
    parser.add_argument("--init_trace", help="set of traces", default=100)
    args = parser.parse_args()

    # init_data = str(args.init_data)
    init_parm = float(args.init_parm)
    init_trace = int(args.init_trace)
 
    # dft = pd.read_csv(init_data)


    
    alpha = init_parm

    dft = pd.read_csv('network_data_lun1.csv')
    dft = dft.sample(frac=1).reset_index(drop=True)
    dft = dft.iloc[0:init_trace]

    t1 = time.time()
    paramet = int(len(dft)*alpha)
    c, ref_c, fix_value1 = algo(dft,paramet)
    t2 = time.time()
    print("In set of trace vel_x :"+str(fix_value1[0])+"; vel_y: "+str(fix_value1[1])+"; decision maker: "+str(fix_value1[2])+"; wind: "+str(fix_value1[3])+" cause is "+str(c), " with number of refienmnets "+ str(ref_c))
    print("time", (t2-t1)*1000)












