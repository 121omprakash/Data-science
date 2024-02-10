# importing a python module
print('Importing Numpy Library'.center(50,'-'))
import numpy 
a = numpy.arange(10,50,3)
print(a)
#importing Inbult python Library
print('Importing Math Library'.center(50,'-'))
import math
print('Nearest grestest value of 25.4 : {}'.format(math.ceil(25.4)))
print('Nearest lowest value of 25.4 : {}'.format(math.floor(25.4)))
print('Returning the wholenumbewr part of 35.78 :{}'.format(math.trunc(35.78)))
print('Using Trigonometric Function'.center(50,'-'))
#using trigonometric function from library
print('Value of Sin(0): {}'.format(math.sin(0)))
print('Value of Cos(0): {}'.format(math.cos(0)))

# importing or using a local file
from Function import factorial
print('Factorial of 10 is : {}'.format(factorial(5)))

# importing  module with alias
import pandas as pd
lst = pd.Series([10,20,30,40,50])
print(lst)