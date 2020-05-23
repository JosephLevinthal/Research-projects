vidai=int(input("quantidade inicial de vida de um personagem"))
d1=int(input("valor sorteado no cubo 1: "))
d2=int(input("valor sorteado no cubo 2: "))
d3=int(input("valor sorteado no cubop3: "))
n= d1+d2+d3
dano= 10*n
vidar=vidai-dano
if (vidai>dano and d1<=12 and d2<=12 and d3<=12):
	print(vidar)
	print("VIVO")
elif (vidai<dano and d1<=12 and d2<=12 and d3<=12):
	vidar=0
	print(vidar)
	print("MORTO")
else:
	print("Entrada invalida")