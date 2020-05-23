from numpy import*

peso = array(eval(input("Digite os pesos: ")))
altura = array(eval(input("Digite as alturas: ")))

for i in range(size(peso)):
	peso[i] = peso[i]/ (altura[i] * altura[i])
	peso[i] = round(peso[i],2)

print(peso)
if(max(peso) < 17):
	x = "MUITO ABAIXO DO PESO"
elif(max(peso) >= 17 and max(peso) <= 18.49):
	x = "ABAIXO DO PESO"
elif(max(peso) >= 18.5 and max(peso) <= 24.99):
	x = "PESO NORMAL"
elif(max(peso) >= 25 and max(peso) <= 29.99):
	x = "ACIMA DO PESO"
elif(max(peso) >= 30 and max(peso) <= 34.99):
	x = "OBESIDADE"
elif(max(peso) >= 35 and max(peso) <= 39.99):
	x = "OBESIDADE SEVERA"
elif(max(peso) > 40):
	x = "OBESIDADE MORBIDA"

	
print("O MAIOR IMC DA TURMA EH:", max(peso))
print(x)