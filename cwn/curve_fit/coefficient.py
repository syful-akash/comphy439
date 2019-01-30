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