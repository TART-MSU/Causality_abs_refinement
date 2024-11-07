<h1 align="center"><a href="https://ieeexplore.ieee.org/document/10745858">Efficient Discovery of Actual Causality using
Abstraction-Refinement</a></h1>

## Introduction
In this repository, you can explore our case studies and their implementation. This repository first presents some visual results observed in the causal analysis part of the paper. It then provides a guide for the implementation of the proposed algorithm on three case studies: Lunar Lander and Mountain Car from OpenAI Gym, and F16 autopilot simulator [link](https://github.com/stanleybak/AeroBenchVVPython.git).

## Causal Analysis

<p float="left">
  <img src="figs/lunar_good.gif" width="49%" />
  <img src="figs/lunar_bad_1.gif" width="49%" /> 
</p>


<br>
<br>
In the above GIF images, you can observe two distinct scenarios: the left one results in success, while the right one ends in failure. In both scenarios, there is a wind blowing from left to right. In the scenario on the right, the lander attempts to counteract the wind by extensively using its right engine, but it overcompensates, causing the lander to tilt and become unstable. Consequently, it drifts too far to the left, missing the landing pad and crashing. In the scenario on the left, the lander effectively utilizes its right engine to maintain control and successfully lands. These observations indicate that excessive use of the right engine is the cause of the failure for the lander on the right.




## Experiments
Before running this code, ensure you have installed the required packages listed in `requirements.txt`.


```bash
pip install -r requirements.txt
```

### F16 Autopilot Simulator
#### Generating Data

Now that we have the desired networks, we need to run 2 scenarios to obtain various traces with different initial values. Use the following command to generate tarces for first scenario:
```bash
python /f16/traces/gen_sc1.py
```
To generate traces for a second scenario, use the command below:
```bash
python /f16/traces/gen_sc2.py
```
#### Run Experiments
To run experiments with the **Abs_DA** algorithm mentioned in the paper, use the code below. You can adjust the value of alpha (`α`) in the range [0, 1] and the number of traces in the range [0, 9500] (Fisrt Scenario), [0,22500] (Second Scenario):

Fisrt Scenario:

```bash
python /f16/src/first_scenario/f16_abs_da.py --init_parm=<α> --init_trace=<No. traces>  
```
Second Scenario:
```bash
python /f16/src/second_scenario/f16_abs_da_1.py --init_parm=<α> --init_trace=<No. traces>  
```



To run experiments with the **Abs_Z3** algorithm mentioned in the paper, use the code below. You can adjust the value of alpha (`α`) in the range [0, 1] and the number of traces in the range [0, 9500] (Fisrt Scenario), [0,22500] (Second Scenario):
```bash
python /f16/src/first_scenario/f16_abs_z3.py --init_parm=<α> --init_trace=<No. traces>  
```
Second Scenario:
```bash
python /f16/src/second_scenario/f16_abs_z3_1.py --init_parm=<α> --init_trace=<No. traces>  
```
To run experiments with the **Only_DA** and **Only_Z3** algorithm mentioned in the paper, use the code below: You can adjust the value the number of traces in the range [0, 9500] (Fisrt Scenario), [0,22500] (Second Scenario):

Fisrt Scenario:
```bash
python /f16/src/first_scenario/f16_da.py --init_trace=<No. traces>  
python /f16/src/first_scenario/f16_z3.py --init_trace=<No. traces>  
```

Second Scenario:
```bash
python /f16/src/second_scenario/f16_da.py --init_trace=<No. traces>  
python /f16/src/second_scenario/f16_z3.py --init_trace=<No. traces>  
```
*Note: The provided data include around 9000 traces. However, you can generate additional traces using the generating codes in `f16/src/fisrt_scenario/sc1_data.csv` `f16/src/second_scenario/sc2_data.csv`.*


### Lunar Lander
#### Generating Data
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
#### Run Experiments
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
*Note: The provided data include around 9000 traces. However, you can generate additional traces using the generating codes in `Lunar_lander/traces`.*

### Mountain Car
#### Generating Data
Same as Lunar Lander we begin with generating traces, to generate traces , use the command below:
```bash
python /Mountain_car/traces/gen_traces.py
```
*Note: You can also modify the initial velocity (`vel`) and initial position (`pos`) inside the for loop in lines 14-18 of `/Mountain_car/traces/gen_traces.py`. Currently, they are set as `pos=[-1.2, -1.1, ..., 0.6]` and `vel=[-0.07, -0.06, ..., 0.07]`.*

#### Run Experiments
To run experiments with the **Abs_DA** algorithm mentioned in the paper, use the code below. You can adjust the value of alpha (`α`) in the range [0, 1] and the number of traces in the range [0, 10280]:
```bash
python /Mountain_car/src/abs_da.py --init_parm=<α> --init_trace=<No. traces>  
```
To run experiments with the **Abs_Z3** algorithm mentioned in the paper, use the code below. You can adjust the value of alpha (`α`) in the range [0, 1] and the number of traces in the range [0, 10280]:
```bash
python /Mountain_car/src/abs_z3.py --init_parm=<α> --init_trace=<No. traces>  
```
To run experiments with the **Only_DA** and **Only_Z3** algorithm mentioned in the paper, use the code below: You can adjust the value the number of traces in the range [0, 10280]:
```bash
python /Mountain_car/src/da.py --init_trace=<No. traces>  
python /Mountain_car/src/z3.py --init_trace=<No. traces>  
```
*Note: The provided data include around 10000 traces. However, you can generate additional traces using the generating codes in `Mountain_car/traces`.*

## Citation
If you find this paper and repository useful for your research, please consider citing the paper using BibTex below:
```
@ARTICLE{rafieioskouei2024causality,
  author={Rafieioskouei, Arshia and Bonakdarpour, Borzoo},
  journal={IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems}, 
  title={Efficient Discovery of Actual Causality Using Abstraction Refinement}, 
  year={2024},
  volume={43},
  number={11},
  pages={4274-4285},
  doi={10.1109/TCAD.2024.3448299},
  ISSN={1937-4151},
  month={Nov}}
```
