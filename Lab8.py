"""
CS2302
Lab8
Purpose: The purpose of this lab is to write a program that “discovers” 
trigonometric identities and tests all combinations of the trigonometric 
expressions provided. As well as creating another program that solves the 
partition problem using backtracking. 
Created on May 1, 2019
Olac Fuentes
@author: Nancy Hernandez
"""

import random
import numpy as np
import math
from math import *
from mpmath import *

def equal(f1, f2, tries = 1000, tolerance = 0.0001):
    for i in range(tries):
        t = random.uniform(-math.pi, math.pi)
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1 - y2) > tolerance:
            return False
    print(t)
    return True

def subsetsum(S, last, goal):
    if goal == 0:
        return True, []
    if goal < 0 or last < 0:
        return False, []
    res, subset = subsetsum(S, last - 1, goal - S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S, last - 1, goal) # Don't take S[last]

def edit_distance(s1, s2):
    # Computes edit distance from string s1 to string s2 using dynamic programming
    # Returns edit distance matrx from string s1 to string s2
    # The actual edit distance is stored in d[-1,-1]
    d = np.zeros((len(s1) + 1, len(s2) + 1), dtype = int)
    d[0, :] = np.arange(len(s2) + 1)
    d[:, 0] = np.arange(len(s1) + 1)
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                d[i, j] = d[i - 1, j - 1]
            else:
                n = [d[i, j - 1], d[i - 1, j - 1], d[i - 1, j]]
                d[i, j] = min(n) + 1       
    return d

S = [3, 1, 5, 9, 12] 

n = len(S) 

trigExpression = ['sin(t)', 'cos(t)', 'tan(t)', 'sec(t)', '- sin(t)', '- cos(t)', '- tan(t)', 'sin(-t)', 
                  'cos(-t)', 'tan(-t)', 'sin(t)/cos(t)', '2 * sin(t / 2) * cos(t / 2)', 'sin(t)* sin(t)', 
                  '1 - cos(t) * cos(t)', '(1 - cos(2 * t)) / 2', '1 / cos(t)']

#To find all the different comparisons
for i in range(len(trigExpression)):
    for j in range(len(trigExpression)):
        print(equal(trigExpression[i], trigExpression[j]))
       
#part two of lab 8
for i in range(100):
    print('Goal =', i)
    a, s = subsetsum(S, len(S) - 1, i)
    if a:
        print('Solution:', s)
    else:
        print('There is no solution')