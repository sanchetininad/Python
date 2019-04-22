# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 23:03:09 2019

@author: nsancheti
"""

#We use pandas library for data structures and analysis
import pandas as pd

#read the objects' weights and values
data = pd.read_csv("50 item Knapsack.csv")
wt = data['Weight']
val = data['Value']

#define the weight constraint of the knapsack
Weight_Capacity = 1000
temp_total = Weight_Capacity

#define dictionaries and lists for memoizing
mem = dict()
save = dict()
output = list()

#define the recursive function for knapsack
def rec(wt, val, mem, temp_total, i):
    key = str(temp_total) + ':' + str(i)
    #return any previously calculated (memoized) solutions
    if key in mem:
        return mem[key]
    #define the limiting cases
    elif temp_total == 0:
        return 0
    elif temp_total < 0:
        return 0
    elif i<0:
        return 0
    #if there is no capacity for the
    elif temp_total< wt[i]:
        to_return = rec(wt, val, mem, temp_total, i - 1)
    else:
        a = rec(wt, val, mem, temp_total - wt[i], i - 1) + val[i]
        b = rec(wt, val, mem, temp_total, i - 1)
        to_return = max(a, b)
        if a > b:
            save[key] = 1
        else:
            save[key] = 0
    
    mem[key] = to_return    
    
    return to_return

rec(wt, val, mem, temp_total, len(wt) - 1)

#retrieve the optimal basket of products
temp_total = Weight_Capacity
i = len(wt) - 1
while i >= 0 and temp_total > 0:
    if save[str(temp_total)+':'+str(i)]==1:
        output.append((data.Object[i]))
        temp_total = temp_total - wt[i]
    i = i-1
print('Objects in optimal solution are',output)
     


