from numpy import *
massa=array(eval(input('Diite o seu peso:   ')))
altura = array(eval(input('Diite o seu altura:   ')))
imc=zeros(size(massa))
for i in range(size(massa)):
	imc[i] = massa[i] / (altura[i]*altura[i])
print(around(imc,2))
print("O MAIOR IMC DA TURMA EH:",round(max(imc),2))
if(max(imc)<17):
	print("MUITO ABAIXO DO PESO")
elif(17<= max(imc) and max(imc) <=18.49):
	print("ABAIXO DO PESO")
elif(18.5 <= max(imc) and max(imc) <= 24.99):
	print("PESO NORMAL")
elif(25<=max(imc)and max(imc) <=29.99):
	print("ACIMA DO NORMAL")
elif(30<=max(imc)and max(imc) <= 34.99):
	print("OBESIDADE")
elif(35<=max(imc) and max(imc) <=39.99):
	print("OBESIDADE SEVERA")
else:
	print("OBESIDADE MORBIDA")

			


	
	