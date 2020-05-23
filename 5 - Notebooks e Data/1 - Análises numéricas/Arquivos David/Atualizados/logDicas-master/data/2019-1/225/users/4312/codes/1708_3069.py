x = input("nome do ataque: ")
d1 = int(input("valor do dado 1: "))
d2 = int(input("valor do dado 2: "))

if(d1 >= 1 and d1 <= 8 d2 >= 1 and d2 <= 8):
	if(x == "FURIA"):
		g = 10 + (d1 +d2)
		print(g)
   elif(x == "GRITO"):
		g = 6 + (d1 + d2)
		print(g)
   elif(x == "TOQUE"):
		g = (d1 + d2)**2
		print(g)
else:
	  print("Entrada invalida")