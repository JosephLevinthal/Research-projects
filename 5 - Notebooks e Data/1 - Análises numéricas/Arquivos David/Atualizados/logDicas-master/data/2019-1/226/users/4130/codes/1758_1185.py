from numpy import *

glic = array(eval(input("Vetor de glicose: ")))

i = 0
cont = 0

while(i < size(glic)):
	if(glic[i] > 99):
		print(i)
		cont = cont + 1
	i = i + 1
print(cont)