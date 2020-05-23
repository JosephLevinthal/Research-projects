from numpy import *
p = array(eval(input("digite: ")))
a = array(eval(input("digite: ")))

v = zeros(size(p), dtype=float)

for i in range(size(p)) and range(size(a)):
	imc = p[i] / a[i]**2
	v[i] = round(imc, 2)
	imc = 0

print(v)
print("O MAIOR IMC DA TURMA EH:", max(v))

if (max(v) < 17):
	print("MUITO ABAIXO DO PESO")
elif (17 <= max(v) <= 18.49):
	print("ABAIXO DO PESO")
elif (18.5 <= max(v) <= 24.99):
	print("PESO NORMAL")
elif (25 <= max(v) <= 29.99):
	print("ACIMA DO PESO")
elif (30 <= max(v) <= 34.99):
	print("OBESIDADE")
elif (35 <= max(v) <= 39.99):
	print("OBESIDADE SEVERA")
elif (max(v) > 40):
	print("OBESIDADE MORBIDA")
