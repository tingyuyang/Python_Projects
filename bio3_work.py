# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:36:12 2016

@author: student
"""
def reveComp(x):
    Str =list(x)
    i=0
    while i<len(Str):
        if Str[i]=='T':
            Str[i]='A'
        elif (Str[i]=='A'):
            Str[i]='T'
        elif (Str[i]=='C'):
            Str[i]='G'
        elif (Str[i]=='G'):
            Str[i]='C'
        i=i+1
    Str =''.join(Str)
    Str = Str[::-1]
    print(Str)
