from numpy import *
v = array(eval(input("digite os numeros reais positivos: ")))
i = 0
p1 = 0
while(i<size(v)):
	p1 = p1 + (v[i])**(1/6)
	i = i + 1
M = (p1/size(v))**6
print(round(M,2))