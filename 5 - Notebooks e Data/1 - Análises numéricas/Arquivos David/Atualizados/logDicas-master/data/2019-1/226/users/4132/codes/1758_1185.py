from numpy import *

v = array(eval(input("Diigte glicoes: ")))

i = 0
cont = 0

while( i < size(v) ):
	if(v[i]>99):
		cont+=1
		print(i)
	i+=1
print(cont)
