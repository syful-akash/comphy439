#!/usr/bin/python
'''
Importing necessary python builtin library
'''
import matplotlib.pyplot as plt
'''Importing self written python script from current directory
which work as the main linear least square function'''
from least_square import least_square

'''
This is the begining of the program. The data here I used from 3rd year
2nd semester lab where we determine "Reactance due to inductance"  
'''
x=[100,200,250,300,350,400,450,500,600,650,700,750,800,850,900,950,1000]
y=[2.22,4.84,6.6,6.46,8.25,10.20,11.45,12.33,13.33,14.31,16.21,18.05,18.95,19.85,20.73,21.61,22.48]

'''this section is written for taking data from user. uncomment the folling 
5 lines to fell the test of it. Precaution: it will kill your time. 
'''
# print("Give your two data point for x & y respectively (separate two entry by space)")
# print(">>>", end=" ")
# x = [float(i) for i in input().split()]
# print(">>>", end=" ")
# y = [float(i) for i in input().split()]

'''
Show Linear least square fit 
'''
plt.title('Least Square Method(Linear Fit) for Reactance due to inductance')
plt.xlabel('Frequeccy')
plt.ylabel('Inductive Reactance')
plt.show(least_square(x,y,1))