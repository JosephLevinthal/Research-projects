# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
H = float(input("Digite a H: "))
h = float(input("Digite a h: "))
r = float(input("Digite a r: "))

print("Entradas:",H,",",h,",",r)

if(H<0 or h<0 or r<0 or H<h or H<2*r ):
   print("Entradas invalidas")
elif(h==r):
	# se altura do nivel for igual ao raio o volume vai ser metade da esfera
	volume = (4/3*pi*r**3)/2
	print("Volume:",round(volume*1000,3),"litros")
elif(h>r and h<=(H-r)):
	# se altura de nivel for maior que o raio e menor ou igual a altura total menos o raio superior
	volume = ((4/3*pi*r**3)/2) + pi*r**2*(h-r)
	print("Volume:",round(volume*1000,3),"litros")
elif(h>(H-r)):
	x = H-h
	volume = pi*r**2*(h-r) + (4/3*pi*r**3) - pi/3*x**2*(3*r-x)
	print("Volume:",round(volume*1000,3),"litros")
	 
