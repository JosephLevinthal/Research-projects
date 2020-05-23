from numpy import*
numeros=array(eval(input("numeros: ")))
n=size(numeros)
cont=0
m=0
while(cont<n):
	m=(1/numeros[cont])+m
	cont=cont+1
print(round(n/m, 2))
