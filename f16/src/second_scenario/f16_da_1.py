import pandas as pd
import time 
import argparse



def Algo_n_abs(df):
    df2 = df.loc[df['result'] == False]
    
    f = open("result_da_1.txt", "a")
    

    t1 = time.time()
    for index, row in df2.iterrows():
        roll_value = row['roll']
        speed_value = row['speed']
        power_value = row['power']
        pit_value = row['pit']
        aoa_value = row['aoa']
        slip_value = row['slip']


        
        df_checka = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] == speed_value ) & (df['power'] != power_value) & (df['pit'] == pit_value) & (df['aoa'] == aoa_value) & (df['slip'] == slip_value) ]

        df_checkb = df.loc[(df['result'] == False) & (df['roll'] != roll_value) & (df['speed'] != speed_value ) & (df['power'] == power_value) & (df['pit'] != pit_value) & (df['aoa'] != aoa_value) & (df['slip'] != slip_value)]

        if len(df_checka) > 0 and len(df_checkb) > 0:
            f.write("Cause is power : "+ str(power_value)+"\n")
            pass
        

        df_check1a = df.loc[(df['result'] == True) & (df['roll'] != roll_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value) & (df['aoa'] == aoa_value) & (df['slip'] == slip_value) ]

        df_check1b = df.loc[(df['result'] == False) & (df['roll'] == roll_value) & (df['speed'] != speed_value ) & (df['power'] != power_value) & (df['pit'] != pit_value) & (df['aoa'] != aoa_value) & (df['slip'] != slip_value)]
        if len(df_check1a) > 0 and len(df_check1b) > 0:
            f.write("Cause is roll : "+ str(roll_value)+"\n")
            pass
        

        df_check2a = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] != speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value) & (df['aoa'] == aoa_value) & (df['slip'] == slip_value)]

        df_check2b = df.loc[(df['result'] == False) & (df['roll'] != roll_value) & (df['speed'] == speed_value ) & (df['power'] != power_value) & (df['pit'] != pit_value) & (df['aoa'] != aoa_value) & (df['slip'] != slip_value)]
        if len(df_check2a) > 0 and len(df_check2b) > 0:
            f.write("Cause is speed : "+ str(speed_value)+"\n")
            pass

        df_check3a = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] != pit_value) & (df['aoa'] == aoa_value) & (df['slip'] == slip_value)]

        df_check3b = df.loc[(df['result'] == False) & (df['roll'] != roll_value) & (df['speed'] != speed_value ) & (df['power'] != power_value) & (df['pit'] == pit_value) & (df['aoa'] != aoa_value) & (df['slip'] != slip_value)]
        if len(df_check3a) > 0 and len(df_check3b) > 0:
            f.write("Cause is pit : "+ str(pit_value)+"\n")
            pass

        df_check4a = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value) & (df['aoa'] != aoa_value) & (df['slip'] == slip_value)]

        df_check4b = df.loc[(df['result'] == False) & (df['roll'] != roll_value) & (df['speed'] != speed_value ) & (df['power'] != power_value) & (df['pit'] != pit_value) & (df['aoa'] == aoa_value) & (df['slip'] != slip_value)]
        if len(df_check4a) > 0 and len(df_check4b) > 0:
            f.write("Cause is aoa : "+ str(pit_value)+"\n")
            pass

        df_check5a = df.loc[(df['result'] == True) & (df['roll'] == roll_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value) & (df['aoa'] == aoa_value) & (df['slip'] != slip_value)]

        df_check5b = df.loc[(df['result'] == False) & (df['roll'] != roll_value) & (df['speed'] != speed_value ) & (df['power'] != power_value) & (df['pit'] != pit_value) & (df['aoa'] != aoa_value) & (df['slip'] == slip_value)]
        if len(df_check5a) > 0 and len(df_check5b) > 0:
            f.write("Cause is slip : "+ str(pit_value)+"\n")
            pass



    f.close()
    t2 = time.time()
    t = t2-t1
    
    f.close()





if __name__ == '__main__':

    parser = argparse.ArgumentParser()


    parser.add_argument("--init_trace", help="set of trace", default=22000)
    args = parser.parse_args()

    
    init_trace = int(args.init_trace)
 
    dft = pd.read_csv('result_case2.csv')


    dft = dft.iloc[0:init_trace]
    
    t1 = time.time()
    Algo_n_abs(dft)
    t2 = time.time()
    # print('time:', (t2-t1)*1000)
    # print('Cause in traces saved in file result_da_1.txt')