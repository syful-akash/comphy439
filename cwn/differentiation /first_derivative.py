from numpy import sin,cos,tan,pi, arange
import matplotlib.pyplot as plt 
# def fx(x,h):
#     y_h=sin(x+h)
#     y_x=sin(x)
#     return y_h,y_x
h=0.00001
x=[]
y=[]
y_x=[]

for i in arange(-1*pi,2*pi,h):
    x.append(i)
    y_h=sin(i+h)
    y_i=sin(i)

    dx=(y_h-y_i)/h
    y_x.append(dx)
    y.append(y_i)
    # print(i)

# print(x, end="")
plt.plot(x,y,label='Sin')
plt.plot(x,y_x,label='Derivative')
plt.legend()
plt.show()