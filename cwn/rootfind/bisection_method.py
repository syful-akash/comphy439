from sympy import *



def f(a):
    x,y,z=symbols('x,y,z')
    # expr=x*x-2*x-3
    expr=simplify(str_expr)
    b=expr.subs(x,a)
    return b


def bisection(domain):
    count = 0
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

str_expr=input('''Polynoial is 
>>''')
print("Give your domain")
print(">>>", end=" ")
domain = [float(i) for i in input().split()]

print(bisection(domain))