a = float(input("valor disponivel?"))
b = int(input("Quantidade de ru que deseja?"))
c = float(input("valor do ticket?"))
d= int(input("quantidade de passe de onibus?"))
e = float(input("valor do passe?"))

if a >= (b*c) + (d*e):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"
print(mensagem)
	

