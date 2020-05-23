n = int(input("digite os valores de n:"))

cont = 1  #var cont

ap = 3 #aproximacoes

while (cont < n):
	#denominador
	x = (cont * 2) * (cont * 2 + 1) * (cont * 2 + 2)
	
	#ap de pi
	ap = ap + (-1) ** (cont  + 1) * 4 / x
	cont = cont + 1
	
print(round(ap,8))




		  