# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:57:07 2016

@author: tingyuyang
"""
def dH (s,t):
    count = 0
    n=0
    for r in str(s):
        if r != t[n]:
            count += 1
        n=n+1
            
    return count
