a = float(input("aceleracao: "))
vel0 = float(input("vel inicial: "))
n = int(input("digite n: "))
from numpy import *
i = 0
t = arange(n)
d = zeros(n)
while(i<size(t)):
	d[i] = ((a * t[i]**2)/2) + vel0 * t[i]
	i = i+1
print(d)