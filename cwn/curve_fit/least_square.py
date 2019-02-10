'''Importing builtin python library'''
import numpy as np
import matplotlib.pyplot as plt
'''importing self written python script from current directory'''
from linear_fit import linear_fit
from coefficient import coefficient

'''defining main linear least square function'''
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
   # print(x_new) # this command was written as check purpus
    # print(y_new) # this command was written as check purpus
    plt.plot(x, y, 'ko', label='Data') #ploting raw data as black dot
    plt.plot(x_new, y_new, label='Linear Fit') #ploting linear fit for given data 
    plt.legend()
    
    