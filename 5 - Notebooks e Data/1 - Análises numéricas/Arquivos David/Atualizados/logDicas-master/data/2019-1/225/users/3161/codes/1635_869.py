valor = float(input("digite um numero: "))

if(valor >= 200):
	mensagem = valor - (valor*5/100)
else:
	mensagem = valor
print(round(mensagem, 2))