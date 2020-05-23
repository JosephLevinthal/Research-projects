from numpy import *
vet1=array(eval(input("digite o numero de gols: ")))
vet2=array(eval(input("digite o numero de gols pegos: ")))

v=0
e=0
d=0
i=0
vet3= vet1 - vet2
for elemento in vet3:
	if(elemento>0):
		v=v+1
	elif(elemento<0):
		d=d+1
	elif(elemento==0):
		e=e+1
p=zeros(3, dtype=int)
p[0]= v
p[1]= e
p[2]= d
print(p)
