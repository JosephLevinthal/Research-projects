from numpy import *
from math import *

peso = array(eval(input()))
altura = array(eval(input()))
n = size(peso)
cont=zeros(n,dtype=float)

for i in range(size(peso)):
	cont[i] = peso[i]/(altura[i]*altura[i])
	
for j in range(size(cont)):
	cont[j] = round(cont[j],2)

print(cont)

print("O MAIOR IMC DA TURMA EH:", max(cont))

if(max(cont)<17):
	print("MUITO ABAIXO DO PESO")
elif(17<=max(cont)<=18.49):
	print("ABAIXO DO PESO")
elif(18.5<=max(cont)<=24.99):
	print("PESO NORMAL")
elif(25<=max(cont)<=29.99):
	print("ACIMA DO PESO")
elif(30<=max(cont)<=34.99):
	print("OBESIDADE")
elif(35<=max(cont)<=39.99):
	print("OBESIDADE SEVERA")
else:
	print("OBESIDADE MORBIDA")
