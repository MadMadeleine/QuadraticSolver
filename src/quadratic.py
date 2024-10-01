''' Quadratic.py Solves ax^2 + bx + c = 0 and returns the result '''

import numpy as np

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

print('The equation is: ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0')

root1 = float((-b + np.sqrt((b ** 2) - (4*a*c)))/(2*a))
root2 = float((-b - np.sqrt((b ** 2) - (4*a*c)))/(2*a))

print('The roots of the eqaution are: ' + str(root1) + ', ' + str(root2))
