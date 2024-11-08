import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from collections import deque, namedtuple
import numpy as np
import random
import copy
import gym
import matplotlib.pyplot as plt
import time
import os
import re
import pandas as pd




class Model(nn.Module):
    def __init__(self, state_size, action_size, layer_sizes):
        super(Model, self).__init__()
        self.seed = torch.manual_seed(42)

        layers = [nn.Linear(state_size, layer_sizes[0])]
        for i in range(1, len(layer_sizes)):
            layers.append(nn.Linear(layer_sizes[i - 1], layer_sizes[i]))
        layers.append(nn.Linear(layer_sizes[-1], action_size))

        self.layers = nn.ModuleList(layers)

    def forward(self, state):
        for layer in self.layers[:-1]:
            state = F.relu(layer(state))
        action_values = self.layers[-1](state)
        return action_values

class ReplayBuffer:
    def __init__(self, buffer_size, action_size):
        self.seed = random.seed(42)
        self.action_size = action_size
        self.memory = deque(maxlen=buffer_size)
        self.experiences = namedtuple("Experiences", field_names=["state","action","reward","new_state", "done"])
        
    def add(self, state, action, reward, new_state, done):
    # Convert state and new_state to NumPy arrays if they are tuples
        if isinstance(state, tuple):
            state = np.array(state[0]) if len(state) > 0 else np.array([])
        if isinstance(new_state, tuple):
            new_state = np.array(new_state[0]) if len(new_state) > 0 else np.array([])

        e = self.experiences(state, action, reward, new_state, done)
        self.memory.append(e)


        
    def sample(self, batch_size):
        experiences = random.sample(self.memory, k=batch_size)
        
        states = torch.from_numpy(np.vstack([e.state for e in experiences if e is not None])).float().to(device)
        actions = torch.from_numpy(np.vstack([e.action for e in experiences if e is not None])).long().to(device)
        rewards = torch.from_numpy(np.vstack([e.reward for e in experiences if e is not None])).float().to(device)
        new_states = torch.from_numpy(np.vstack([e.new_state for e in experiences if e is not None])).float().to(device)
        dones = torch.from_numpy(np.vstack([e.done for e in experiences if e is not None]).astype(np.uint8)).float().to(device)
        
        return states, actions, rewards, new_states, dones
    
    def __len__(self):
        return len(self.memory)
class DQNAgent:
    def __init__(self, state_size, action_size, layer_sizes):
        self.seed = random.seed(42)
        self.action_size = action_size
        
        self.local_nn = Model(state_size, action_size, layer_sizes).to(device)
        self.target_nn = Model(state_size, action_size, layer_sizes).to(device)
        
        self.optimizer = optim.Adam(self.local_nn.parameters(), lr=LR)
        
        self.memory = ReplayBuffer(BUFFER_SIZE, action_size)
        
        self.t_step = 0

        
        
    def step(self, state, action, reward, new_state, done):
        self.memory.add(state, action, reward, new_state, done)
        
        self.t_step = (self.t_step + 1) % UPDATE_EVERY
        if self.t_step == 0:
            if len(self.memory) > BATCH_SIZE:
                experiences = self.memory.sample(BATCH_SIZE)
                self.learn(experiences, GAMMA)
                
    def act(self, state, eps=0.):
    
        if not isinstance(state, np.ndarray):
            state = np.array(state[0]) if type(state) is tuple else np.array(state)
        
        state = torch.from_numpy(state).float().unsqueeze(0).to(device)
        self.local_nn.eval()
        with torch.no_grad():
            action_values = self.local_nn(state)
        self.local_nn.train()
        
        
        if random.random() > eps:
            return np.argmax(action_values.cpu().data.numpy())
        else:
            return random.choice(np.arange(self.action_size))

        
    def learn(self, experiences, gamma):
        states, actions, rewards, new_states, dones = experiences
        
        Q_target = self.target_nn(new_states).detach().max(1)[0].unsqueeze(1)
        Q_target_value = rewards + (gamma * Q_target * (1-dones))
        
        Q_exp = self.local_nn(states).gather(1, actions)
        loss = F.mse_loss(Q_exp, Q_target_value)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        self.soft_update(self.local_nn, self.target_nn, TAU)
        
    def soft_update(self, local_nn, target_nn, tau):
        for local_nn_params, target_nn_params in zip(local_nn.parameters(), target_nn.parameters()):
            target_nn_params.data.copy_(tau*local_nn_params.data + (1.0-tau)*target_nn_params.data)




def dqn(net_name):
    flag = 0
    n_episodes = 1000
    score_deque = deque(maxlen=100)
    scores = []
    eps = 1.0
    decay = 0.995
    min_eps = 0.005
   
    
    for i_episode in range(n_episodes):
        state = env.reset()  
        done = False
        score = 0 
        start_time = time.time()
        while not done:
            if time.time()-start_time>5:
                state = env.reset()  
                done = False
                score = 0
                start_time = time.time()
                continue
            action = agent.act(state, eps)
            next_state, reward, done, _ = env.step(action)[:4]  
            agent.step(state, action, reward, next_state, done)
            state = next_state  
            score += reward
            if done:
                break
        
                
        score_deque.append(score)
        scores.append(score)
        
        eps = max(min_eps, eps*decay)
        
        print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(score_deque)), end="")
        if i_episode % 100 == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(score_deque)))
        if np.mean(score_deque)>=200.0:
            print('\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}'.format(i_episode-100, np.mean(score_deque)))
            torch.save(agent.local_nn.state_dict(), net_name)
            flag = 1
            break
    if flag ==0:
        torch.save(agent.local_nn.state_dict(), net_name)
    return scores

if __name__ == '__main__':

    filenames = []
    filenames = []
    pwd = os.getcwd()
    pwd = os.path.join(pwd, 'lun_model')
    for path, subdirs, files in os.walk(pwd):
        for filename in files:
            f = os.path.join(filename)
            filenames.append(f)
        filenames.pop(0)
        filenames.pop(0)
        filenames.pop(0)
        for i in filenames:
            for x in range(-30,30,5):
                vel_x = float(x/10)
                for y in range(-30,30,5):
                    vel_y = float(y/10)
                    
                    numbers = re.findall(r'\d+', i)  
                    array = [int(num) for num in numbers] 
                    wind = array[-1]
                    array.pop()
                    net = array.copy()

                    device = torch.device('cpu')

                

                    print('Runing on {} with vel_x :{}, vel_y :{}, wind :{}'.format(i,vel_x,vel_y,wind))


                    env = gym.make('LunarLander-v2',enable_wind= True,wind_power=wind)

                    state = env.reset()

                    action_size = env.action_space.n

                    state_low = env.observation_space.low
                    state_high = env.observation_space.high
                    state_size = len(state_low)



                    BUFFER_SIZE = int(1e5)
                    BATCH_SIZE = 64
                    GAMMA = 1.0
                    UPDATE_EVERY = 4
                    TAU = 1e-3
                    LR = 5e-4



                    layer_sizes = net
                    agent = DQNAgent(state_size, action_size, layer_sizes)

                    

                    state = env.reset()
                    lander = env.unwrapped.lander
                    
                    lander.linearVelocity = (vel_x, vel_y)
                    done = False
                    score = 0 
                    st = 'lun_model/'+i
                    
                    agent.local_nn.load_state_dict(torch.load(st,map_location=torch.device('cpu')))
                    count = 0
                    for s in range(1):
                        start_time = time.time()
                        flag = 0
                        while not done:
                            if time.time()-start_time>25 and flag ==0:
                                flag =1
                                start_time = time.time()
                                state = env.reset()
                                lander = env.unwrapped.lander
                                
                                lander.linearVelocity = (vel_x, vel_y)
                                done = False
                                score = 0 
                                st = 'lun_model/'+i
                                agent.local_nn.load_state_dict(torch.load(st,map_location=torch.device('cpu')))
                                continue
                            if time.time()-start_time>25 and flag ==1:
                                break
                            
                            env.render()
                            action = agent.act(state)
                            state, reward, done, _ = env.step(action)[:4]
                            score += reward
                            if done:
                                if score >100:
                                    count =1
                                break
                    listi =[]
                    if count == 1:
                        outcome =True
                    else:
                        outcome = False
                    listi.append([i,vel_x,vel_y,wind,outcome])

                    column_names = ["network","vel_x","vel_y","wind","result"]

                    df = pd.DataFrame(listi, columns=column_names)
                    size = i[:-4]

                    filename = 'data_lun_T/data_'+size+str(vel_x)+'_'+str(vel_y)+'wind'+str(wind)+'.csv'
                    


                    df.to_csv(filename, index=False)
                    
                                
                    env.close()



