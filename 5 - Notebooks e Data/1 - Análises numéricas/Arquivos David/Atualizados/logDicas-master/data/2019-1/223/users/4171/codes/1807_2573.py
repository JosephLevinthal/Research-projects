from numpy import *

massa = array(eval(input("massa dos alunos: ")))
altura = array(eval(input("altura dos alunos: ")))
v = zeros(size(massa))
i = 0

for i in range(size(massa)):
	
	imc = massa[i] / altura[i] **2
	v[i] = round(imc,2)

print(v)
print("O MAIOR IMC DA TURMA EH: ", max(v))

if max(v) < 17:
	print("MUITO ABAIXO DO PESO")
elif 17 <= max(v) < 18.5:
	print("ABAIXO DO PESO")
elif 18.5 <= max(v) < 25:
	print("PESO NORMAL")
elif 25 <= max(v) < 30:
	print("ACIMA DO PESO")
elif 30 <= max(v) < 35:
	print("OBESIDADE")
elif 35 <= max(v) < 40:
	print("OBESIDADE SEVERA")
elif max(v) > 40:
	print("OBESIDADE MORBIDA")