# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Digite a altura total do tanque: "))
h = float(input("Digite o nivel de combustivel no tanque: "))
r = float(input("Digite o raio dos bojos semiesfericos inferior e superior: "))
b = 2*r
print("Entradas:",x ,",",h,",",r)
from math import *
# Volume do cilindro:
vc = pi * r **2 * x
# Volume da esfera: 
ve = 4/3 * pi * r **3
# Volume da calota:
v = (pi/3) * (h **2) * (3*r - h)

if ((x==0 or h==0 or r==0) or (x < h or x < b)):
	print("Entradas invalidas")
else:
	if (h <= r):
		v= (pi/3) * (h **2) * (3*r - h)
		print("Volume: ",round (v * 1000, 3),"litros")
	elif(r<h and h<= x -r):
		v = (4 * pi * (r**3)/6) + (pi * (r**2) * (h - r))
		print("Volume: ",round(v* 1000,3), "litros")
	elif(h > x - r):
		v= ((4 * pi * (r**3))/6) + ((pi/3) * (r**2) * (h - r))*2
		print("Volume: ",round(v* 1000,3), "litros")

	
	
	