a = float(input("aceleracao: "))
v0 = float(input("veloc.inicial: "))
N = int(input("n de elemento: "))
from numpy import *
p = 0
b = arange(N)
n=zeros(N)
while(p < N):
	t=b[p]
	dt = (a*(t)**2)/2 + v0*t
	n[p] = b[p]
	p = p + 1
print(n)
