# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:39:05 2016

@author: tingyuyang
"""
def haystack(s,t):
    length = len(t)
    i=0
    for letter in s:
        if s[i:i+length]==t[0:length]:
            print (i+1)
        i=i+1
    return 0
