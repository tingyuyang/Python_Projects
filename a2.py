# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:14:43 2016

@author: Tingyu Yang
"""
#1

from matplotlib import pyplot as plt
import csv
with open('annual.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    rows = [r for r in reader if r[0] == 'GCAG']
years = [row[1] for row in rows]
temps = [row[2] for row in rows]
plt.plot(years, temps)
plt.title('Global Mean Temperatures')
plt.xlabel('Year')
plt.ylabel('Difference from 20th century average ('
       + u'\N{DEGREE SIGN}' + 'C)')
plt.show()

#2
with open('global.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    rows = [r for r in reader]
year = [row[0] for row in rows]
total = [row[1] for row in rows]
plt.plot(year, total)
plt.title('Total Carbon Emission')
plt.xlabel('Year')
plt.ylabel('Carbon Emissions from fossil fuel consumption and cement production')
plt.show()

#3

with open('guns.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    rows = [r for r in reader
        if r['Average firearms per 100 people'] != '']
def rate(row):
    return float(row['Average firearms per 100 people'])
decreasing = sorted(rows, key=rate, reverse=True)
decreasing = decreasing[:20]
ISO_code =[d['ISO code'] for d in decreasing]
firearm =[d['Average firearms per 100 people'] for d in decreasing]
fire =[]
i=0
for item in firearm:
    fire.append(float(firearm[i]))
    i=i+1
xs = [i+0.1 for i, _ in enumerate(fire)]
plt.bar(xs,fire)
plt.title('ISO code')
plt.xticks([i+0.5 for i, _ in enumerate(ISO_code)],ISO_code)
plt.show()

#4

with open('iris.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    rows = [r for r in reader]
sepal_length = [r[0] for r in rows]
sepal_width = [r[1] for r in rows]
plt.scatter(sepal_length,sepal_width)
plt.title("Scatter Plot")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()

