a = int(input("escreva a quantidade de votos de Ambrosio: "))
b = int(input("escreva a quantidade de votos de Demelza: "))
total = a + b

if (a > 50/100 * total):
	mensagem = "Ambrosio Rutra"
	pv = (a / total) * 100
else:
	mensagem = "Demelza Olecram"
	pv = (b / total) * 100
print(mensagem)
print(round(pv, 2))
		