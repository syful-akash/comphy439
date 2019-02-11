'''
This Pyhton Script is written as
the assignment 2 computational physics course
at Dept. of Physics,
SUST, Sylhet - 3114, Bangladesh.

(c) Md. Syful Islam
(syfulakash@gmail.com)
Reg. no: 2015132022
Student, Department of Physics,
SUST, Sylhet - 3114, Bangladesh.

The task is given for this assignment is to find out bond length of NaCl.
The potential function for NaCl is V(r)= - [e^2/(4πεr)]+V0*exp(-r/r0)

'''

'importing python builtin library'
import numpy as np 
from matplotlib import pyplot as plt
from math import exp 
import scipy 

'impoeting self written python script for secant method'
# from secant_method import secant
def v(r):
    v= - 14.4*(1/r)+1090*exp(-r/0.330)
    return v
def f(r):
    '''this is the simplified 1st derivative of potential function
    where e2/4πϵ0=14.4 ̊A eV ,v0=1090 ev and r0=0.330 angstrom
    '''
    f= -(14.4*(1/r*r))+(1090/0.330)*exp(-r/0.330)
    return f   
'''at equilibrium position f(r)=dV(r)/dr=0. so I used secant method to find bond 
length of NaCl. 
'''

def secant(domain):
    count=0
    error=(domain[1]-domain[0])/domain[1]
    tollerence=0.0000000005
    x=[]
    y=[]
    c=[]
    xn=1.0
    while abs(error)>tollerence:
    # while xn>0:
        denominator=f(domain[1])-f(domain[0])
        numerator=(domain[1]-domain[0])*f(domain[1])
        xn=domain[1]-numerator/denominator
        domain[0]=domain[1]
        domain[1]=xn
        error=(domain[1]-domain[0])/domain[1]
        c.append(count) 

        count+=1   

        x.append(xn) 
        y.append(f(xn)) #storing potential at xn
    return xn, x,y,c, count
'''I find bond length of NaCl at equilibrium position in range 0.01 angstrom
to 1.0 an '''
dom=[0.01,1.0] 
blength= secant(dom)
print(f'bond length for NaCl is {blength[0]} angstrom afrte {blength[4]} iteration')
plt.plot(blength[1],blength[2]) #potential distance plot
# plt.plot(blength[1],blength[3])
plt.xlabel('distance(angstrom)')
plt.ylabel('potential(eV)')
plt.title('NaCl Potential vs Distan' )
plt.show()


'''
the result I got as bond length is approximately 1.793671239743739 angstrom 
at equilibrium position but the actual bond length at equilibrium is 2.36 angstrom. 
This may occure for programing error
'''