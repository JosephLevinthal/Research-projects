#ser aprovado com nota mínima 7
from numpy import*

notas = array(eval(input("digite as notas: ")))
while(size(notas)>1):
	ap = 0
	for i in notas: 
		if(i >= 5)and(i<7):
			ap = ap + 1
	print(ap)
	notas = array(eval(input("digite as notas: ")))