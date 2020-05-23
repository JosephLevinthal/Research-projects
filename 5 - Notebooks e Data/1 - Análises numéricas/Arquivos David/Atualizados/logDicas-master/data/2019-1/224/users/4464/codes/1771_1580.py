from numpy import *

vetP = array(eval(input()))
vetN = array(eval(input()))

f = 0
a = 0
r = 0

cont = 0
while(cont < len(vetP)-1):
	if (vetP == -1):
		f += 1
	elif (vetP[cont] < 6):
		r += 1
	else:
		a+=1
	cont+=1
print(f,a,r,cont)