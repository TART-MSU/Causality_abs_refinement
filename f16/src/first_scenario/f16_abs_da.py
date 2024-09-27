import pandas as pd
import sys
import argparse
import time 
import numpy as np

sys.setrecursionlimit(1000)

def over_func(df):
       distances = np.sqrt((df['altitude'].values[:, np.newaxis] - df['altitude'].values) ** 2 +
                     (df['speed'].values[:, np.newaxis] - df['speed'].values) ** 2)


       mask = (distances < 100) & (df['result'].values[:, np.newaxis] == df['result'].values) & \
              (df['power'].values[:, np.newaxis] == df['power'].values) & \
              (df['pit'].values[:, np.newaxis] == df['pit'].values)


       merged_df = df[mask.any(axis=1)].drop_duplicates(subset=['power', 'pit', 'result'])

       return merged_df

def MMC1(df,dataorginal):
    df2 = df.loc[df['result'] == False]
    
    counterexmaple1 = dataorginal
    counterexmaple2 = dataorginal
    counterexmaple3 = dataorginal
    counterexmaple4 = dataorginal
    for index, row in df2.iterrows():
        altitude_value = row['altitude']
        speed_value = row['speed']
        power_value = row['power']
        pit_value = row['pit']
        fix_value = [altitude_value,speed_value,power_value,pit_value]
        
        
        df_checka = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] == speed_value ) & (df['power'] != power_value) & (df['pit'] == pit_value)]

        if len(df_checka) > 0 :
            
            cause = power_value
            var = 'power'
            return True ,cause , var, fix_value
        else:
            counterexmaple1  = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] == speed_value ) & (df['power'] != power_value) & (df['pit'] == pit_value)]





        df_checka = df.loc[(df['result'] == True) & (df['altitude'] != altitude_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value)]
 
        if len(df_checka) > 0 :
            
            cause = altitude_value
            var = 'altitude'
            return True ,cause , var, fix_value
        else:
            counterexmaple2  = df.loc[(df['result'] == True) & (df['altitude']!= altitude_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value)]

        


        df_checka = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] != speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value)]
 
        if len(df_checka) > 0 :
            
            cause = speed_value
            var = 'speed'
            return True ,cause , var, fix_value
        else:
            counterexmaple3  = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] != speed_value ) & (df['power'] == power_value) & (df['pit'] == pit_value)]


        
        df_checka = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] != pit_value)]
 
        if len(df_checka) > 0 :
            cause = pit_value
            var = 'pit'
            return True ,cause , var, fix_value
        else:
            counterexmaple4  = df.loc[(df['result'] == True) & (df['altitude'] == altitude_value) & (df['speed'] == speed_value ) & (df['power'] == power_value) & (df['pit'] != pit_value)]

        

    counterexample = min(counterexmaple1,counterexmaple2,counterexmaple3,counterexmaple4,key=len)
    return False , counterexample , None, None

def MMC2(dataorginal,var,cause,fix_value):
    
    altitude_value = fix_value[0]
    speed_value  = fix_value[1]
    power_value = fix_value[2]
    pit_value = fix_value[3]
    
    if var == 'power':
        df_checkb = dataorginal.loc[(dataorginal['result'] == False) & (dataorginal['altitude'] != altitude_value) & (dataorginal['speed'] != speed_value ) & (dataorginal['power'] == power_value) & (dataorginal['pit'] != pit_value)]
        if len(df_checkb)>0:
            return True
        else:
            return False
    elif var == 'altitude':
        df_checkb = dataorginal.loc[(dataorginal['result'] == False) & (dataorginal['altitude'] == altitude_value) & (dataorginal['speed'] != speed_value ) & (dataorginal['power'] != power_value) & (dataorginal['pit'] != pit_value)]
        if len(df_checkb)>0:
            return True
        else:
            return False
    elif var == 'speed':
        df_checkb = dataorginal.loc[(dataorginal['result'] == False) & (dataorginal['altitude'] != altitude_value) & (dataorginal['speed'] == speed_value ) & (dataorginal['power'] != power_value) & (dataorginal['pit'] != pit_value)]
        if len(df_checkb)>0:
            return True
        else:
            return False
    else:
        df_checkb = dataorginal.loc[(dataorginal['result'] == False) & (dataorginal['altitude'] != altitude_value) & (dataorginal['speed'] != speed_value ) & (dataorginal['power'] != power_value) & (dataorginal['pit'] == pit_value)]
        if len(df_checkb)>0:
            return True
        else:
            return False





    
def under_approx(df,parm,refie_c):
    while True:
        refie_c = refie_c + 1
        data = df[0:int(parm)]
        
        res, cause_or_counter,var,fix_value = MMC1(data,df)
        if res == True:
            return data , cause_or_counter , refie_c , var , fix_value
        else:
            parm = int(parm*1.1)
            continue
            


def over_approx(causet,datat,dft,ref_c,var,fix_value):
    ref_c = ref_c+1
    dft = over_func(dft)
    res = MMC2(dft,var,causet,fix_value)
    if res == True:
        return True , causet, ref_c, fix_value
    else:
        return False, causet, ref_c, fix_value 
    
def algo(dft,paramet):
    datat , causet, ref_c ,var, fix_value1 =  under_approx(dft,paramet,0)
    
    res, c, ref_c, fix_value1 = over_approx(causet,datat,dft,ref_c,var,fix_value1)
    if res==True:
        return c, ref_c, fix_value1
    else:
        return algo(dft,paramet*1.5)
 
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--init_parm", help="param", default=0.01)
   
    parser.add_argument("--init_trace", help="set of traces", default=7000)
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
    print("In set of tarce altitude :"+str(fix_value1[0])+"; speed: "+str(fix_value1[1])+"; power: "+str(fix_value1[2])+"; pit: "+str(fix_value1[3])+" cause is " +str(c), " with number of refienmnets "+ str(ref_c))
    print('time',(t2-t1)*1000)



