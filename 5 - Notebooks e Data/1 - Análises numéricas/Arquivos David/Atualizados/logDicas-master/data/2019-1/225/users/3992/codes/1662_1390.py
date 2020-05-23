tempo = float(input("minutos consumidos: "))

if (tempo <= 100):
	         preco = tempo*1.20
else:
				preco = tempo*1.40 + 25
print(round(preco, 2))
				