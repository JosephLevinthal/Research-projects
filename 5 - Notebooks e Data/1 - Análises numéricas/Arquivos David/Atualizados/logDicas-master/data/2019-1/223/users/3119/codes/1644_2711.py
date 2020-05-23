#Entradas 
valor = int(input("Valor disponivel: "))
quant = int(input("Quantidades de tickets do RU: "))
preco = float(input("Valor dos tickets: "))
passe = int(input("Quantidade de passes de onibus: "))
val = float(input("Valor dos passes: "))
soma = (quant * preco) + (passe * val)

if(soma <= valor):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")