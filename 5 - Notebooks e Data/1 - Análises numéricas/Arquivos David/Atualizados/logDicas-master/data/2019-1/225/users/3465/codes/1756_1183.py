from numpy import *
v1 = array(eval(input("")))
cont = 0
i = 0
while(i<len(v1)):
	if(v1[i]>0):
		cont+=1
	i+=1
copia = array([0]*cont)
i = 0
j =0
while i<len(v1):
	if(v1[i]>0):
		copia[j] = v1[i]
		j+=1
	i+=1
print(copia)