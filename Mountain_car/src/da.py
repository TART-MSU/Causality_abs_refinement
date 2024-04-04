import pandas as pd
import time 
import argparse



def Algo_n_abs(df):
    df2 = df.loc[df['result'] == False]
    
    f = open("result_da.txt", "a")
    

    t1 = time.time()
    for index, row in df2.iterrows():
        pos_value = row['pos']
        vel_value = row['vel']
        network_value = row['network']
        
        df_checka = df.loc[(df['result'] == True) & (df['vel'] == vel_value) & (df['pos'] == pos_value) & (df['network'] != network_value)]
        df_checkb = df.loc[(df['result'] == False) & (df['vel'] != vel_value) & (df['pos'] != pos_value) & (df['network'] == network_value)]
        if len(df_checka) > 0 and len(df_checkb) > 0:
            f.write("Cause is Network : "+ network_value+"\n")
            pass
        df_check1a = df.loc[(df['result'] == True) & (df['vel'] != vel_value) & (df['pos'] == pos_value) & (df['network'] == network_value)]
        df_check1b = df.loc[(df['result'] == False) & (df['vel'] == vel_value) & (df['pos'] != pos_value) & (df['network'] != network_value)]
        if len(df_check1a) > 0 and len(df_check1b) > 0:
            f.write("Cause is vel : "+ str(vel_value)+"\n")
            pass
        df_check2a = df.loc[(df['result'] == True) & (df['vel'] == vel_value) & (df['pos'] != pos_value) & (df['network'] == network_value)]
        df_check2b = df.loc[(df['result'] == False) & (df['vel'] != vel_value) & (df['pos'] == pos_value) & (df['network'] != network_value)]
        if len(df_check2a) > 0 and len(df_check2b) > 0:
            f.write("Cause is pos : "+ str(pos_value)+"\n")
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
    Algo_n_abs(dft)
    t2 = time.time()
    print('time:', (t2-t1)*1000)
    print('Cause in traces saved in file result_da.txt')

