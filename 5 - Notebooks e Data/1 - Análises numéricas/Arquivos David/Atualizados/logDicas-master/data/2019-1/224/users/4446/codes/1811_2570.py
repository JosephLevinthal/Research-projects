from numpy import *
vet=array(eval(input("digite os numeros: ")))
n=size(vet)
m=sum(vet)/n
f=1

for elemento in vet:
	f=abs(elemento-m)*f
p=f**(1/n)
print(round(p, 3))