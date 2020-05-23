from numpy import *
peso = array(eval(input("Digite o peso: ")))
h = array(eval(input("Digite a altura: ")))
imc = zeros(size(peso), dtype=float)
for i in peso:
	imc = peso/(h*h)
	m = round(max(imc), 2)
	if(m < 17):
		sit = "muito abaixo do peso"
	elif(17 <= m <= 18.49):
		sit = "abaixo do peso"	
	elif(18.5 <= m <= 24.99):
		sit = "peso normal"
	elif(25 <= m <= 29.99):
		sit = "acima do peso"
	elif(30 <= m <= 34.99):
		sit = "obesidade"
	elif(35 <= m <= 39.99):
		sit = "obesidade severa"
	elif(m > 40):
		sit = "peso morbida"	
for v in range(size(imc)):
	imc[v] = round(imc[v], 2)
print(imc)
print("O MAIOR IMC DA TURMA EH:", m)
print(sit.upper())