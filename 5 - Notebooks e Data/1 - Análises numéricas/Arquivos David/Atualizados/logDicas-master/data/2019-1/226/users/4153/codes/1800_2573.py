from numpy import *

peso = array(eval(input("Insira o peso: ")))
altura = array(eval(input("Insira a altura: ")))
IMC = zeros(size(peso))
for i in range(size(peso)):
	IMC[i] = round ((peso[i]/(altura[i])**2),2)
print(IMC)
print("O MAIOR IMC DA TURMA EH:",max(IMC))
m = max(IMC)
if(m < 17):
	print("MUITO ABAIXO DO PESO")
elif(m >= 17 and m <= 18.49):
	print("ABAIXO DO PESO")
elif(m >= 18.5 and m <= 24.99):
	print("PESO NORMAL")
elif(m >= 25 and m < 29.99):
	print("ACIMA DO PESO")
elif(m >= 30 and m < 34.99):
	print("OBESIDADE")
elif(m >= 35 and m < 39.99):
	print("OBESIDADE SEVERA")
elif(m >= 40):
	print("OBESIDADE MORBIDA")