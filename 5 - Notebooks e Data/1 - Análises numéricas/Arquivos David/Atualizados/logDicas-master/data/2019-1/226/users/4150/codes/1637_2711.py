a = float(input("valor disponivel: "))
b = int(input("quantidade de tickets: "))
c = float(input("valor dos tickets: "))
d = int(input("passes de onibus: "))
e = float(input("valor do passe: "))

f = (b*c) + (d*e)

if (a>f):
	mensagem = "SUFICIENTE"
	
else:
	mensagem = "INSUFICIENTE"

print(mensagem)
