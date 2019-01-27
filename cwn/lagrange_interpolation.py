'''
Lagrange interpolation of the order of n has been
developed here. This program is used as a sample in
computational physics course at Dept. of Physics,
SUST, Sylhet - 3114, Bangladesh.

(c) Md. Enamul Hoque
(mjonyh@gmail.com)
Lecturer, Department of Physics,
SUST, Sylhet - 3114, Bangladesh.
'''

'Importing library'
import matplotlib.pyplot as plt

def lagrange_poly(point, x, f):
	'''This is the main function where lagrange interpolation
	is implemented. This function return the value of f(x)
	correspondce to the x within the domain.'''
	result = 0
	
	'Loop over j for summation'
	for j in range(len(x)):
		p = 1
		
		'Loop over k for product'
		for k in range(len(x)):
		
			'Checking the condition for k and j'
			if k != j:
				p *= float(point - x[k])/float(x[j] - x[k]) 
		result += p * f[j]
		
	return result
	
def lagrange_dataset(x,y):
	'This function generate new Dataset for lagrange interpolation'
	initial = x[0]
	dx = float(x[1]-x[0])/10
	n_x = []
	n_y = []

	while initial < x[len(x)-1]+1:
		n_x.append(initial)
		n_y.append(lagrange_poly(initial, x, y))
		initial += dx
	
	return n_x, n_y

'''
This is the begining of the program
'''
x = [1,2,6]
y = [1,3,9]

'Calling new dataset from lagrange interpolation'
n_x, n_y = lagrange_dataset(x,y)
print(n_x)
print(n_y)

'Ploting data and interpolated data'
plt.plot(x,y, 'ko')
plt.plot(n_x, n_y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation')
plt.show()

