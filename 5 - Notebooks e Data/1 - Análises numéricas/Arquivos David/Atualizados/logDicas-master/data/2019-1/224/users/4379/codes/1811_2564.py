from numpy import *
gols_feitos=array(eval(input("digite o vetor: ")))
gols_sofridos=array(eval(input("digite o vetor: ")))
resultado= gols_feitos-gols_sofridos
i=0
v=0
e=0
d=0
for l in resultado:
	if(l==0):
		e=e+1
	elif(l>0):
		v=v+1
	else:
		d=d+1
z = zeros(3,dtype = int)
z[0] = v
z[1] = e
z[2] = d
print(z)
	
		
	