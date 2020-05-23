from numpy import *
s=input("digite a palavra que devera ser traduzida: ")
vet=array(eval(a,e,i,o,u))
i=0
n=""
for j,i in zip(s,i):
	if(j==vet[i]):
		n=n+s.replace(j, "")
	else:
		n=n+j
print(n)