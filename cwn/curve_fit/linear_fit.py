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