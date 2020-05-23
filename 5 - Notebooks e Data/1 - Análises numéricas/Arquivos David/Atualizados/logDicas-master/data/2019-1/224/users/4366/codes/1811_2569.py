from numpy import*
from math import*
n=array(eval(input("digite um vetor de numeros reais: ")))
soma=sum(n)
cont=0
media=soma/size(n)
for i in n:
	cont = cont + (i - media)**2
	d = sqrt(cont/(size(n)-1))
print(round(d, 3))