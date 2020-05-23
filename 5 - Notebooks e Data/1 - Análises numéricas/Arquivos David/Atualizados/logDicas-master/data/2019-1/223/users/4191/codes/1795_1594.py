from numpy import*

vet=array(eval(input("Danos: ")))

i=0
peso=1
dano=0
while(i<size(vet)):
	dano=dano+vet[i]*peso
	peso=peso+1
	i=i+1
	
print(dano)	