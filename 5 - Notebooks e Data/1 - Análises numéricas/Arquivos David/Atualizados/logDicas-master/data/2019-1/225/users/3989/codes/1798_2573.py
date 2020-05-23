from numpy import*
v1 = array(eval(input("")))
v2 = array(eval(input("")))
imc = zeros(size(v1), dtype=float)

for i in range(len(v1)):
	imc[i] = round(v1[i]/(v2[i] * 2),2)
print(imc)
print("O MAIOR IMC DA TURMA EH: ", imc.max())
print (imc.max())
if (imc.max())<=17:
	print("MUITO ABAIXO DO PESO")
elif (imc.max())<=18.49:
	print("ABAIXO DO PESO")
elif (imc.max())<=24.99:
	print("PESO NORMAL")
elif (imc.max())<=29.99:
	print("ACIMA DO PESO")
elif (imc.max())<=34.99:
	print("OBESIDADE")
elif(imc.max())<=39.99:
	print("OBESIDADE SEVERA")
else:
	print("OBESIDADE MORBIDA")
	
	
	
	




	



