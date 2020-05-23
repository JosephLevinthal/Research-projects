valor = float(input("digite valor: "))
quantru = int(input("digite ru: "))
valtickets = float(input("digite valor tickets: "))
quantonibus = int(input("digite quantidade onibus: "))
valpasses = float(input("digite passes: "))
formula = ((quantru*valtickets)+(quantonibus*valpasses)))

if(formula):
	mensagem = ("SUFICIENTE")
else:
	mensagem = ("INSUFICIENTE")

print(mensagem)