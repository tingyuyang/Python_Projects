# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 19:11:23 2016

@author: benphanson
"""

import csv
import math

with open('abalone_data.csv', 'r') as f:
   reader = csv.reader(f, delimiter=',')
   rows = [r for r in reader]
   
rings = [float(row[8]) for row in rows]
length = [float(row[1])for row in rows]
sex = [row[0] for row in rows]
male = [r for r in sex if r[0] == 'M']
large = [float(r) for r in length if r > 0.5239920995930099]


def mean(x):
    return sum(x) / len(x)
    
def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
    
def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
 
def prob(x,y):
    return len(x) / len(y)
       
    
print ("Mean rings = {}".format(mean(rings)))
print ("Median rings = {}".format(median(rings)))
print ("StDev of rings = {}".format(standard_deviation(rings)))
print ("Correlation of rings and length = {}".format(correlation(rings,length)))
probability_male = prob(male,sex)
probability_large = prob(large,length)
print ("Probability male = {}".format(probability_male))
print ("Probability large = {}".format(probability_large))
probability_maleAndLarge = probability_male * probability_large
probability_maleOrLarge = probability_male + probability_large
probability_male_given_large = probability_maleAndLarge / probability_large
probability_large_given_male = probability_large / probability_maleAndLarge
print ("Probability male and large = {}".format(probability_maleAndLarge))
print ("Probability male or large = {}".format(probability_maleOrLarge))
print ("Probability male given large = {}".format(probability_male_given_large))
print ("Probability large given male = {}".format(probability_large_given_male))
