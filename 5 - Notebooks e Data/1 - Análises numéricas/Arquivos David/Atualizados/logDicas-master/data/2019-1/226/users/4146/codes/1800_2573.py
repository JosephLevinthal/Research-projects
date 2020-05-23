from numpy import *
m = array(eval(input("Massas: ")))
h = array(eval(input("Alturas: ")))

imc = zeros(size(m))

for i in arange(size(m)):
	x = round((m[i]/h[i]**2), 2)
	imc[i] = imc[i] + x

for i in range(size(imc)):
	if(max(imc) < 17):
		msg = "MUITO ABAIXO DO PESO"
	elif(17 <= max(imc) <= 18.49):
		msg = "ABAIXO DO PESO"
	elif(18.5 <= max(imc) <= 24.99):
		msg = "PESO NORMAL"
	elif(25 <= max(imc) <= 29.99):
		msg = "ACIMA DO PESO"
	elif(30 <= max(imc) <= 34.99):
		msg = "OBESIDADE"
	elif(35 <= max(imc) <= 39.99):
		msg = "OBESIDADE SEVERA"
	else:
		msg = "OBESIDADE MORBIDA"
		
print(imc)
print("O MAIOR IMC DA TURMA EH: ", max(imc))
print(msg)
	