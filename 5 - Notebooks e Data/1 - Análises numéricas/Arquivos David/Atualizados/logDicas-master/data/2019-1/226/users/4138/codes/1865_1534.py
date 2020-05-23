from numpy import *

x = float(input("inisra o numero:"))
k = int(input("insira:"))
a = 0
i = 0
tg = x**(2*i + 1)/(2*i + 1)

for i in range(k):
	tg = (x**(2*i+1))/((2*i+1))
	a = a + tg
	i = i + 1
print(round(a,7))