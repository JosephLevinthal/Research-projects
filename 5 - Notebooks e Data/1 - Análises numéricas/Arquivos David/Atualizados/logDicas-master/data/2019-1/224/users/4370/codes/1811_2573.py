from numpy import *
peso = array(eval(input("digite o vetor de pesos: ")))
altura = array(eval(input("digite o vetor de alturas: ")))
z = zeros(size(peso),dtype = float)
zpos = 0
for i,j in zip(peso,altura):
	imc = i/j**2
	z[zpos] = round(imc,2)
	zpos = zpos + 1
print(z)
print("O MAIOR IMC DA TURMA EH:",max(z))
if(max(z) < 17):
	print("MUITO ABAIXO DO PESO")
elif(17 < max(z) < 18.49 ):
	print("ABAIXO DO PESO")
elif(18.5 < max(z) < 24.99):
	print("PESO NORMAL")
elif(25 < max(z) < 29.99):
	print("ACIMA DO PESO")
elif(30 < max(z) < 34.99):
	print("OBESIDADE")
elif(35 < max(z) < 39.99):
	print("OBESIDADE SEVERA")
else:
	print("OBESIDADE MORBIDA")