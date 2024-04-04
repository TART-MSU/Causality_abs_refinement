import pandas as pd
from z3 import *
import time 
import argparse

def Algo_n_abs_z3(df):
    
    df2 = df.loc[df['result'] == False]
    
    f = open("result_z3.txt", "a")
    

    t1 = time.time()


    for index, row in df2.iterrows():
        
        network_var = String('network')
        pos_var = Real('pos')
        vel_var = Real('vel')
        result_var = Bool('result')


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
            result_value = bool(model.eval(result_var))

            result_row = df.loc[(df['network'] != row['network']) & (df['pos'] == row['pos']) & (df['vel'] == row['vel']) & (df['result'] == True)]
            if len(result_row) > 0:
                f.write("Cause is Network : "+ str(row['network'])+"\n")
                pass
        
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
            result_value = bool(model.eval(result_var))

            result_row = df.loc[(df['network'] == row['network']) & (df['pos'] != row['pos']) & (df['vel'] == row['vel']) & (df['result'] == True)]
            if len(result_row) > 0:
                f.write("Cause is pos : "+ str(row['pos'])+"\n")
                pass
        

        network_var = String('network')
        pos_var = Real('pos')
        vel_var = Real('vel')
        result_var = Bool('result')


        solver = Solver()


        network_constraint = network_var == row['network']
        pos_constraint = pos_var == row['pos']
        vel_constraint = vel_var != row['vel']
        result_constraint = result_var == True

        # Add constraints to the solver
        solver.add(network_constraint)
        solver.add(pos_constraint)
        solver.add(vel_constraint)
        solver.add(result_constraint)

        
        if solver.check() == sat:
            
            model = solver.model()
            network_value = model.eval(network_var).as_string()
            pos_value = float(model.eval(pos_var).numerator_as_long()) / float(model.eval(pos_var).denominator_as_long())
            vel_value = float(model.eval(vel_var).numerator_as_long()) / float(model.eval(vel_var).denominator_as_long())
            result_value = bool(model.eval(result_var))

            result_row = df.loc[(df['network'] == row['network']) & (df['pos'] != row['pos']) & (df['vel'] != row['vel']) & (df['result'] == True)]
            if len(result_row) > 0:
                f.write("Cause is vel : "+ str(row['vel'])+"\n")
                pass

    f.close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    
    parser.add_argument("--init_trace", help="set of trace", default=100)
    args = parser.parse_args()

    
    init_trace = int(args.init_trace)
    
 
    dft = pd.read_csv('network_data.csv')

    dft = dft.sample(frac=1).reset_index(drop=True)


    dft = dft.iloc[0:init_trace]

    
    t1 = time.time()
    Algo_n_abs_z3(dft)
    t2 = time.time()
    print('time:', (t2-t1)*1000)
    print('Cause in traces saved in file result_z3.txt')

    