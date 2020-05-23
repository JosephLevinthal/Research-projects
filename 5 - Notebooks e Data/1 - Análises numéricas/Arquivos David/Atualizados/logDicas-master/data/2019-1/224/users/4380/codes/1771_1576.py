from numpy import *
e=array(eval(input("jogadas eusapia: ")))
b=array(eval(input("jogadas barsanulfo: ")))
posicao=0
ve=0
vb=0
x=int(input("indice do vetor: "))
while (posicao<size(e)):
	if (e[x]>b[x]):
		print("EUSAPIA")
	elif (e[x]<b[x]):
		print("BARSANULFO")
	else:
		print("EMPATE")