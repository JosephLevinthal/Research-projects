from numpy import *

vetorN = array(eval(input("digite vetor: ")))

p = 0
o = 0

while(size(vetorN) > p):
	if(vetorN[p] > 99):
		print(p)
		p = p + 1
		o = o +1
	else:
		p = p +1

print(o)
	

