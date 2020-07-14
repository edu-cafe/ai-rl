# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:41:16 2020

@author: shkim
"""


import gym
import numpy as np
import random

env = gym.make('CartPole-v1')
goal_steps = 500
episode = 0

while True:
  obs = env.reset()
  episode += 1
  for i in range(goal_steps):
    obs, reward, done, info = env.step(random.randrange(0, 2))
    print("episode:", episode, "steps:", i, "  states:", obs, "reward:", reward, "done:", done)
    if done: 
        print("--->episode:", episode, "steps:", i, "  states:", obs, "reward:", reward, "done:", done)
        break
    env.render()


#%%
"""
states(obs) : [카트 위치, 카트 속도, 막대의 각도, 끝에서의 막대의 속도]
reward : 오래 버티는게 목표이며, 보상은 막대가 떨어지지 않는 이상 한 턴을 버텼으므로 1이 주어짐 
done : 막대가 떨어졌는지를 의미함. 이 프로젝트에서 막대가 떨어졌다고 말하는 조건은, 
       막대의 각도가 12도 이상 기울었거나, 카트가 2.4칸 이상 움직인 경우(화면에서 나간 경우) 떨어졌다고 판단
"""