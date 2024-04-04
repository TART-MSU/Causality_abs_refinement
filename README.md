# Experiments
In this repository, you can explore our implementation for our study.
Before running this code, ensure you have installed the required packages listed in `requirements.txt`.


```bash
pip install -r requirements.txt
```

## Car Mountain

## Lunar Lander
### Generating Data
To begin generating traces, we first need to train the networks. For this purpose, you can use the `network_train.py` script.<br>
*Note: You can modify the neural network architecture in `network_train.py` by adjusting the `networks` variable in lines 181-188. Similarly, you can customize the `wind` variable by defining a list for it.*
```bash
python /Lunar_lander/traces/network_train.py
```
Now that we have the desired networks, we need to run different scenarios to obtain various traces with different initial values for vertical speed (`vel_y`) and horizontal speed (`vel_x`). Use the following command to achieve this:
```bash
python /Lunar_lander/traces/gen_trace.py
```
To generate traces for a single scenario, use the command below:
```bash
python /Lunar_lander/traces/single_gen_trace.py
```
*Note: The operations mentioned above might take a long time to complete. You can use pre-trained networks and traces located in `Lunar_lander/traces/networks` for networks and `/Lunar_lander/traces/trace_log` for traces to save time.*
### Run Experiments
To run experiments with the **Abs_DA** algorithm mentioned in the paper, use the code below. You can adjust the value of alpha (`α`) in the range [0, 1] and the number of traces in the range [0, 8980]:
```bash
python /Lunar_lander/src/abs_da.py --init_parm=<α> --init_trace=<No. traces>  
```
To run experiments with the **Abs_Z3** algorithm mentioned in the paper, use the code below. You can adjust the value of alpha (`α`) in the range [0, 1] and the number of traces in the range [0, 8980]:
```bash
python /Lunar_lander/src/abs_z3.py --init_parm=<α> --init_trace=<No. traces>  
```
To run experiments with the **Only_DA** and **Only_Z3** algorithm mentioned in the paper, use the code below: You can adjust the value the number of traces in the range [0, 8980]:
```bash
python /Lunar_lander/src/da.py --init_trace=<No. traces>  
python /Lunar_lander/src/z3.py --init_trace=<No. traces>  
```
*Note: The provided traces include around 9000 traces. However, you can generate additional traces using the generating codes in `Lunar_lander/traces`.*

