from numpy import *

x = array(eval(input(" ")))
y = zeros(size(x), dtype = int)

j = 0
for i in range(size(x)):
	j -= 1
	y[i] = x[j]

print(y)