import math
r= float(input("valor do raio: "))
h= float(input("Altura: "))
n= int(input("Numero da opcao desejada: (1 ou 2)? "))
vesf = (4 * (math.pi) * (r ** 3) / 3)
vcal = (((math.pi) * (h ** 2)) * ((3 * r) - h))/ 3
vcom = vesf - vcal
if (n == 1):
	v = vcal
else:
	v = vcom
print(round(v, 4))
