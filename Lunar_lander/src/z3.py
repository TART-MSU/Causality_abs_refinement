import pandas as pd
from z3 import *
import time 
import argparse

def Algo_n_abs_z3(df):
    # print(df)
    df2 = df.loc[df['result'] == False]
    # print(df2)
    f = open("result_z3.txt", "a")
    #f1 = open("time.txt","a")

    t1 = time.time()


    for index, row in df2.iterrows():
        
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

            result_row = df.loc[(df['result'] == True) & (df['vel_x'] == row['vel_x']) & (df['vel_y'] == row['vel_y'] ) & (df['network'] != row['network']) & (df['wind'] == row['wind'])]


            
            if len(result_row) > 0:
                f.write("Cause is Network : "+ str(row['network'])+"\n")
                pass
        
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

            result_row1 = df.loc[(df['result'] == True) & (df['vel_x'] != row['vel_x']) & (df['vel_y'] == row['vel_y'] ) & (df['network'] == row['network']) & (df['wind'] == row['wind'])]


            
            if len(result_row1) > 0:
                f.write("Cause is vel_x : "+ str(row['vel_x'])+"\n")
                pass
        

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

            result_row2 = df.loc[(df['result'] == True) & (df['vel_x'] == row['vel_x']) & (df['vel_y'] != row['vel_y'] ) & (df['network'] == row['network']) & (df['wind'] == row['wind'])]


            
            if len(result_row2) > 0:
                f.write("Cause is vel_y : "+ str(row['vel_y'])+"\n")
                pass
        

        network_var = String('network')
        vel_x_var = Real('vel_x')
        vel_y_var = Real('vel_y')
        result_var = Bool('result')
        wind_var = Real('wind')


        solver = Solver()

        network_constraint = network_var != row['network']
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
        

            result_row3 = df.loc[(df['result'] == True) & (df['vel_x'] == row['vel_x']) & (df['vel_y'] == row['vel_y'] ) & (df['network'] == row['network']) & (df['wind'] != row['wind'])]


            
            if len(result_row3) > 0:
                f.write("Cause is wind : "+ str(row['wind'])+"\n")
                pass






if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    
    parser.add_argument("--init_trace", help="set of trace", default=100)
    args = parser.parse_args()

    
    init_trace = int(args.init_trace)
    
 
    dft = pd.read_csv('network_data_lun1.csv')

    dft = dft.sample(frac=1).reset_index(drop=True)


    dft = dft.iloc[0:init_trace]

    
    t1 = time.time()
    Algo_n_abs_z3(dft)
    t2 = time.time()
    print('time:', (t2-t1)*1000)
    print('Cause in traces saved in file result_z3.txt')