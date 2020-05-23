mulher = input("S OU N ?") 
ingresso = float(input("valor do ingresso? "))
quantidade = int(input("quantos voce deseja? "))
resultado = ingresso * quantidade
if (mulher == "S"):
	print(round(resultado * 0.8, 2))
else:
	print(round(resultado, 2))