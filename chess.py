# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:16:59 2021

@author: hariramg
"""

import gym
import gym_chess
import random

env = gym.make('Chess-v0')
print(env.render())

env.reset()
done = False

while not done:
    action = random.sample(env.legal_moves)
    env.step(action)
    print(env.render(mode='unicode'))

env.close()