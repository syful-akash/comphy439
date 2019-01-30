import numpy as np
import matplotlib.pyplot as plt
'''
Least Square Method for Linear fit has been
developed here. This Pyhton Script is written as
the assignment computational physics course
at Dept. of Physics,
SUST, Sylhet - 3114, Bangladesh.

(c) Md. Syful Islam
(syfulakash@gmail.com)
Reg. no: 2015132022
Student, Department of Physics,
SUST, Sylhet - 3114, Bangladesh.
'''

'importing necessary Library'

'Defining Function'
def coefficient(x, y):
    '''This function determine the four coefficients
    of linear fit which is used to find a_0 & a_1
    of the linear fit y=a_0+a_1*x and return them
     as c1, c2,c3 & c4
    '''
    c1 = c2 = c3 = c4 = 0.0
    for i in range(len(x)):
        c1 += x[i]
        c2 += x[i]*x[i]
        c3 += y[i]
        c4 += x[i]*y[i]

    return c1, c2, c3, c4

def linear_fit(a, b, x):  # a,b,x represent a_0, a_1 & data set x[]
    '''This Function produce data for different y=a_0+a_1*x
    to corresponding x and return new data point for linear fit
    as x_n & y_n
    '''
    x_n = []
    y_n = []
    i = x[0]-1

    for i in x:
        y = a+b*i
        y_n.append(y)
        x_n.append(i)
       

    return x_n, y_n

def least_square(x, y, degree):

    '''
    calling coefficient function 
    '''
    c1, c2, c3, c4 = coefficient(x, y)
    # print(c1,c2,c3,c4)

    ''' Determining a_0 & a_1 for the linear fit y=a_0+a_1*x'''
    a_0 = (c1*c4-c2*c3)/(c1*c1-len(x)*c2)
    # print(a_0)  # this command was written as check purpus
    a_1 = (c1*c3-len(x)*c4)/(c1*c1-len(x)*c2)
    # print(a_1) #this command was written as check purpus

    '''
    Calling linear_fit to produce data for best Linear fit
    '''
    y_new = []
    x_new = []
    x_new, y_new = linear_fit(a_0, a_1, x)
    'this command was written as check purpus'
    # print(x_new) 
    # print(y_new)
    
    '''
    Ploting Old data point & best linear fit for 
    this data points
    '''
    plt.title('Least Square Method(Linear Fit)')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.plot(x, y, 'ko', label='Data')
    plt.plot(x_new, y_new, label='Linear Fit')
    plt.legend()
    # plt.grid(True)

'''
This is the begining of the program
'''
x=[4,5,7,3]
y=[6,9,0,3]
# print("Give your two data point for x & y respectively (separate two entry by space)")
# print(">>>", end=" ")
# x = [float(i) for i in input().split()]
# print(">>>", end=" ")
# y = [float(i) for i in input().split()]

lsm= least_square(x,y,1)

plt.show(lsm)
