import matplotlib.pyplot as plt 

x=[0,0.2,0.4,0.6,0.8,1,2,3,4,5,6,7,8,9,10]
y=[0,0.5,1,1.4,1.8,2.1,3,3.3,3.4,3.4,3.4,3.4,3.4,3.4,3.4,]

if len(x)==len(y):
    print(True)

plt.plot(x,y)
plt.show()