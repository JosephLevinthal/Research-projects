from numpy import *

v=array(eval(input("numeros reais:")))
t=0
i=0
while(t >= 0):
	
	M=((v[i] ** (-1)) / v) ** (-1)
	cont=cont + 1
print(round(M,2))