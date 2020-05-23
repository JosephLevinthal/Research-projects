from numpy import *
x = array(eval(input()))

a = (sum(x) - min(x))
b = size(x)
c = b - 1
d = a/c
print(round(d,2))