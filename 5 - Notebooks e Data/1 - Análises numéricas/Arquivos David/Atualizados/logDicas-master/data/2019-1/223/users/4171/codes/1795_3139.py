from numpy import *

v = array(eval(input("vetor contendo numeros reais positivos: ")))

i = 0
tg = 0

while i < size(v):
	if dtype(v[i]) == float:
		tg += (v[i]**(1/3))
		
		x = tg 
		
		i += 1
	
M = (x/size(v))**3

print(round(M,2))