# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:44:51 2021

@author: hariramg
"""
import time

from multiprocessing import Pool

def f(x):
    return x*x

x = [100]*1000

start = time.time()
with Pool(5) as p:
    a = p.map(f, [100]*1000)
    
end = time.time()

print(end-start)
   
