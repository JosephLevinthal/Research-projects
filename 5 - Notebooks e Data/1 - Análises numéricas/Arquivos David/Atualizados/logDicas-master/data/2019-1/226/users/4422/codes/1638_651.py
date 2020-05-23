altura = float(input("Qual a Altura? "))
sexo = input("Qual o sexo? (M/F)")

if(sexo == "m".upper()):
	mu = (62.1 * altura) - 44.7
	print(round(mu, 2))
	
else:
	h = (72.7 * altura) - 58
	print(round(h, 2))