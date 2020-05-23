from math import*
n=int(input())
a=factorial(365)
b=365-n
c=factorial(b)
d=365**n
f=c*d
g=1-a/f
h=(g*100)
print(round(h, 2))
