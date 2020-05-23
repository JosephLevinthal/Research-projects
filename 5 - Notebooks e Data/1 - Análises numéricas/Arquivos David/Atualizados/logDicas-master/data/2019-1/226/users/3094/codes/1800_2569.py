from numpy import *
from math import *
v= array(eval(input("")))
b = sum(v)/size(v)
i = 0
for z in v:
	i = i + (z - b)**2
i = sqrt(i/(size(v) - 1))
print(round(i,3))