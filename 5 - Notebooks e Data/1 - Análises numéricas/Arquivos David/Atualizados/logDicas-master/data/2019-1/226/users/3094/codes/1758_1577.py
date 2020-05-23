from numpy import *

acel = float(input(''))
veloc = float(input(''))
n = int(input(''))

t = arange(n)
d = zeros(n, dtype = int)

d = ((acel*t**2)/2) + veloc * t 
print(d)