from numpy import *

a = float(input("Digite a: "))
vo = float(input("Digite vo : "))
n = int(input("Digite n: "))
v = arange(n,dtype=float)
#d = zeros(n)
i=0

while(i<size(v)):
	v[i]=(a*i**2)/2 + vo*i
	i=i+1
print(v)