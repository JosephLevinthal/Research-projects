# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

H = float(input("altura: "))               #altura total do tanque
h = float(input("nivel de combustivel: ")) #nivel de combsutivel
r = float(input("raio: "))                 #raio dos bojos

print("Entradas: ",H,",",h,",",r)

cilindro_t = pi * (r ** 2) * (H - (r * 2))
esfera = (4*pi *(r ** 3))/3
calota_t = ((pi/3) * (r ** 2)) * ((3 * r) - r) 
cilindro_p = ((pi * (r ** 2) * (h-r)))
calota_p = ((pi/3) * (h ** 2)) * ((3 * r) - h)

if ((H < 0) or (h < 0) or (r < 0)) or (H < h) or (H < 2 * r):
	print("Entradas invalidas")
elif h < r:                         #Calota inferior
	V = calota_p * 1000
	print("Volume:",round(V, 3) ,"litros")
elif h == r:                         #Calota inferior Completa
	V = (esfera / 2) * 1000
	print("Volume:",round(V, 3) ,"litros")
elif h < H - r:
	V = ((esfera / 2) + cilindro_p) * 1000
	print("Volume:",round(V, 3) ,"litros")
elif h == H - r:
	V = ((esfera / 2) + cilindro_t) * 1000
	print("Volume:",round(V, 3) ,"litros")
elif h < H:
	V = ((esfera / 2) + (calota_p) + cilindro_t) * 1000
	print("Volume:",round(V, 3) ,"litros")
else:
	V = ((esfera) + (cilindro_t)-(calota_p)) * 1000
	print("Volume:",round(V, 3) ,"litros")