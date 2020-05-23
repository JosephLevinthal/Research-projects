var1 = float(input("valor disponivel: "))

var2 = int(input("quantidade de tickets: "))

var3 = float(input("valor dos tickets: "))

var4 = int(input("quantidade de passes: "))

var5 = float(input("valor dos passes: "))

total = var2 * var3 + var4 * var5

if (var1 >= total):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"
print(mensagem)