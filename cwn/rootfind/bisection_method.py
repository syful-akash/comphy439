'''Importing necessary library'''
from sympy import *


'defining polynomial'
def f(a):
    x,y,z=symbols('x,y,z')
    'converting string expression to matheatical mathematical expression'
    expr=simplify(str_expr)  
    b=expr.subs(x,a) # a substitute variable x 
    return b #return function value as b at point a 

'defining main function for bisection method'
def bisection(domain):
    count = 0 #this will count the iteration number
    if f(domain[0])*f(domain[1])<0:
        c = (domain[0]+domain[1])/2
        while c!=0:
        
            if f(c)<0:
                domain[0]=c
            elif f(c)>0:
                domain[1]=c
            elif f(c)==0:
                break
        
            count+=1
            c = (domain[0]+domain[1])/2
        return c, count

    else:
        return "root doesn't exit on this given domain"

'taking poly noial as string expression'
str_expr=input('''Polynoial is 
>>''')
'taking domai'
print("Give your domain")
print(">>>", end=" ")
domain = [float(i) for i in input().split()]

'this will give the root of given polynomial at given domain'
print(bisection(domain))