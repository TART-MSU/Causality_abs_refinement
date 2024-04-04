import os
import warnings
warnings.filterwarnings('ignore')

filenames = []
pwd = os.getcwd()
pwd = os.path.join(pwd, 'networks')
os.system('mkdir data_T')
for path, subdirs, files in os.walk(pwd):
   for filename in files:
     f = os.path.join(filename)
     filenames.append(f)
print(filenames)
for x in filenames:
  st = 'data_T/data_'+str(x)
  os.mkdir(st) 
  for i in range(-12,7):
    i = i/10

    for j in range(-7,8):

      j = j/100
      st1 = "python3 hp_gridding.py --init_pos="+str(i)+" --init_vel="+str(j)+" --network_dir=networks --network_name="+x+" --approx_network_dir=approx_networks"
      os.system(st1)


