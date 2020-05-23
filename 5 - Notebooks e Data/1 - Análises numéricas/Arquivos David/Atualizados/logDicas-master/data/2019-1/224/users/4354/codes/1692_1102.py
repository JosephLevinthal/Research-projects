from math import *
# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
H = float(input("altura do tanque: "))
h = float(input("nivel de combustivel do tanque: "))
r = float(input("raio do bojo semiesferico: "))
# verificação se H,h e r são positivos
if(H and h and r > 0):
# verificação se 2*r é maior que H ou se h é maior que H (Caso de invalidez)
	if(2*r >= H or h > H):
		print("Entradas:",H,",",h,",",r)
		print("Entradas invalidas")
# se não forem é caso de validez
	else:
		if(h < r):
			v = (pi / 3 * h ** 2) * (3 * r - h)
			v = v * 1000
			print("Entradas:",H,",",h,",",r)
			print("Volume:",round(v,3),"litros")
		elif(h == r):
			v = (4/3 * pi * r ** 3)/2
			v = v * 1000
			print("Entradas:",H,",",h,",",r)
			print("Volume:",round(v,3),"litros")
# altura do combustível entre r e a altura (H - r, QUE É A ALTURA DO CILINDRO INTERMEDIARIO MAIS O RAIO DA SEMISESFERA INFEIROR)			
		elif(r < h < (H-r)):
			hc = h-r
			v = (4/3 * pi * r ** 3)/2 + pi*r**2*hc
			v = v *1000
			print("Entradas:",H,",",h,",",r)
			print("Volume:",round(v,3),"litros")
		elif(h == (H - r)):
			hc = h - r
			v = (4/3 * pi * r ** 3)/2 + pi*r**2*hc
			v = v * 1000
			print("Entradas:",H,",",h,",",r)
			print("Volume:",round(v,3),"litros")
		elif(h > (H - r)):
			har = H - h
			hc = H - 2*r
			v_ar = (pi / 3 * har ** 2) * (3 * r - har)
			v_total = 4/3 * pi * r **3 + pi*r**2*hc
			v = v_total - v_ar
			v = v * 1000
			print("Entradas:",H,",",h,",",r)
			print("Volume:",round(v,3),"litros")
		elif(h == H):
			hc = H - 2*r
			v = (4/3 * pi * r ** 3) + pi*r**2*hc
			v = v * 1000
			print("Entradas:",H,",",h,",",r)
			print("Volume:",round(v,3),"litros")
		else:
			print("Entradas:",H,",",h,",",r)
			print("Entradas invalidas")
else:
	print("Entradas:",H,",",h,",",r)
	print("Entradas invalidas")
			