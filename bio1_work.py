# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def numc_count(x):
    count ={'A':0, 'C':0, 'G':0, 'T':0}
    
    for n in x:
        count[n]+=1
        
    for n in "ACGT":
        print(count[n],end=" ")
