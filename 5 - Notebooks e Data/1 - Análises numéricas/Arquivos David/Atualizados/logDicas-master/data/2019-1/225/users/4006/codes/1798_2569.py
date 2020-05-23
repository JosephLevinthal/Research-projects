from  math import*
from numpy import*
x = array(eval(input("Valores: ")))
n = size(x)    
m = sum(x/n)
s = 0
for i in range(n):
    s =  s + (x[i] - m)**2
d = ((s / (n-1))**0.5)
print(round(d,3))