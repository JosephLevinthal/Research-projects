import math

r = float(input("Raio: "))
x = float(input("Altura da coluna de ar na parte superior do tanque: "))
opcao = int(input("Opcao (1 - volume de ar / 2 - volume de combustivel): "))

ve = (4 * math.pi * (r ** 3)) / 3
vce = (math.pi * (x ** 2) * ((3 * r) - x)) / 3

if(opcao == 1):
	print(round(vce, 4))
else:
	print(round(ve - vce, 4))