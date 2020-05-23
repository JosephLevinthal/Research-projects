# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

H = float(input("altura do tanque: "))
h = float(input("nivel de compustivel: "))
r = float(input("raio dos bojos semiesfericos: "))
print("Entradas: ", H, h, r)

vo = pi*(r**2)*h
v = (4/3)*pi*(r**3) #esfera
v2= (pi*(h** 2)*(3*r-h))/3 #ar #calora

if (H>0)and(h>0)and(r>0): 
	elif(h < v2):
		vl = v2*1000
		print("Volume: ", round(h,3) ,"litros")