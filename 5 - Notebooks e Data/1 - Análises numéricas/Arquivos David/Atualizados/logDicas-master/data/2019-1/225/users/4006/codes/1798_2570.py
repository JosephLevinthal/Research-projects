from math import*
from numpy import*
x = array(eval(input("Valores: ")))
n = size(x)
m  = sum(x)/n
p = 1
for i in range(n):
    p = p*(abs(x[i] - m))
e = 1/n
p = p**e
print(round(p,3))