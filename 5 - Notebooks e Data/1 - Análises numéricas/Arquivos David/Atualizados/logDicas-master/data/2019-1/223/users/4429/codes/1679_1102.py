# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
H = float(input("altura do tanque: "))
h = float(input("altura do combustivel no tanque: "))
raio = float(input("raio semiesfericos: "))

Vesfera = ((4/3)*pi*(raio**3))
se = (2/3*pi*(raio**3))

if((H <= 0) or (h <=0) or (raio <= 0) or (H <= h) or (H <= 2*raio)):
	print("Entradas:", H,",", h,",", raio)
	print("Entradas invalidas")
elif(h >= raio):
	cil = (pi*(raio**2)*(h-raio)) + se 	
	vcil = 1000*cil
	print("Entradas:", H,",", h,",", raio)
	print("Volume:", round(vcil, 3), "litros")
	
elif(h < raio):
	si = pi/3*(h**2)*(3*raio-h) 	
	vsi = 1000*si
	print("Entradas:", H,",", h,",", raio)
	print("Volume:", round(vsi, 3), "litros")
	
elif(raio > H - h):
	ss = (cil + 2*se)-si
	vss = 1000*ss
	print("Entradas:", H,",", h,",", raio)
	print("Volume:", round(vss, 3), "litros")
	
