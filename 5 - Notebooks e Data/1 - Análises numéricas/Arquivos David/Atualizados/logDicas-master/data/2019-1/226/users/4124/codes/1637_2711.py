valor = float(input("Valor disponivel: "))
ru = int(input("Quantidade de tickets do ru: "))
val_ru = float(input("Valor do ticket do ru: "))
onibus = int(input("Quantidade de passes de onibus: "))
val_pas = float(input("Valor do passe de onibus: "))

if(((ru * val_ru) + (onibus * val_pas)) <= valor):
	print("suficiente".upper())
else:
	print("insuficiente".upper())