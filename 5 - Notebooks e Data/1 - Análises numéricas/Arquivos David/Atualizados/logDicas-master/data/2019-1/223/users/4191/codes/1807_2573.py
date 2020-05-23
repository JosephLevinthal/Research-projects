from numpy import *

peso=array(eval(input("Peso: ")))
altura=array(eval(input("altura: ")))

imc=zeros(size(peso))

for i in range(size(peso)):
	imc[i]=round(peso[i]/altura[i]**2, 2)
	

print(imc)
maior=max(imc)


print("O MAIOR IMC DA TURMA EH: ", maior)

if(maior<17):
	print("MUITO ABAIXO DO PESO")
elif(maior>=17)and(maior<=18.49):
	print("ABAIXO DO PESO")
elif(maior>=18.5)and(maior<=24.99):
	print("PESO NORMAL")
elif(maior>=25)and(maior<=29.99):	
	print("ACIMA DO PESO")
elif(maior>=30)and(maior<=34.99):
	print("OBESIDADE")
elif(maior>=35)and(maior<=39.99):	
	print("OBESIDADE SEVERA")
elif(maior>=40):
	print("OBESIDADE MORBIDA")