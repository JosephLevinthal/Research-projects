from numpy import*
peso = array(eval(input("digite os pesos dos alunos: ")))
altura = array(eval(input("digite a altura dos alunos: ")))
a = zeros(size(peso), dtype=float)
cont = 0
for i,j in zip(peso,altura):
	imc = i /j**2
	a[cont] = round(imc, 2)
	cont = cont + 1
print(a)
print("O MAIOR IMC DA TURMA EH: ", max(a))
if max(a) < 17:
	print("MUITO ABAIXO DO PESO")
elif max(a) > 17 and max(a) < 18.49:
	print("ABAIXO DO PESO")
elif max(a) > 18.5 and max(a) < 24.99:
	print("PESO NORMAL")
elif max(a) > 25 and max(a) < 29.99:
	print("ACIMA DO PESO")
elif max(a) > 30 and max(a) < 34.99:
	print("OBESIDADE")
elif max(a) > 35 and max(a) < 39.99:
	print("OBESIDADE SEVERA")
elif max(a) > 40:
	print("OBESIDADE MORBIDA")