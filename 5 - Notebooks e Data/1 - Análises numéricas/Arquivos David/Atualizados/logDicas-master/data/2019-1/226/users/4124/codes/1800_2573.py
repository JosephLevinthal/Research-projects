from numpy import *
p = array(eval(input("Peso: ")))
h = array(eval(input("Altura: ")))
imc = zeros(size(p), dtype = float)
for i in range(size(p)):
	imc[i] = round(p[i] / (h[i]**2), 2)
print(imc)
print("O MAIOR IMC DA TURMA EH:", max(imc))

if(max(imc) < 17):
	print("MUITO ABAIXO DO PESO")
elif(max(imc) >= 17 and max(imc) <= 18.49):
	print("ABAIXO DO PESO")
elif(max(imc) >= 18.5 and max(imc) <= 24.99):
	print("PESO NORMAL")
elif(max(imc) >= 25 and max(imc) <= 29.99):
	print("ACIMA DO PESO")
elif(max(imc) >= 30 and max(imc) <= 34.99):
	print("OBESIDADE")
elif(max(imc) >= 35 and max(imc) <= 39.99):
	print("OBESIDADE SEVERA")
elif(max(imc) >= 40):
	print("OBESIDADE MORBIDA")