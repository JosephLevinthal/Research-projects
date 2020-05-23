from numpy import*

peso = array(eval(input("Peso: ")))
alt =  array(eval(input("Altura: ")))

imcs = zeros(size(peso), dtype=float)						

for x in range(size(peso)):
	imcs[x] = round(peso[x]/(alt[x]**2), 2)
print(imcs)
print("O MAIOR IMC DA TURMA EH:",max(imcs))

z = max(imcs)
if (z < 17):
	print("MUITO ABAIXO DO PESO")
elif(z >= 17 and z < 18.5):
	print("ABAIXO DO PESO")
elif(z >=18.5 and z < 25):
	print("PESO NORMAL")
elif(z >= 25 and z < 30):
	print('ACIMA DO PESO')
elif(z >= 30 and z < 35):
	print("OBESIDADE")
elif(z >= 35 and z < 40 ):
	print("OBESIDADE SEVERA")
elif(z >= 40):
	print("OBESIDADE MORBIDA")