import matplotlib.pyplot as plt
from least_square import least_square
'''
This is the begining of the program
'''
# x=[4,5,7,3]
# y=[6,9,0,3]
print("Give your two data point for x & y respectively (separate two entry by space)")
print(">>>", end=" ")
x = [float(i) for i in input().split()]
print(">>>", end=" ")
y = [float(i) for i in input().split()]

'calling least_square and passing argument as list x,y & degree of polynomial'
plt.show(least_square(x,y,1))
