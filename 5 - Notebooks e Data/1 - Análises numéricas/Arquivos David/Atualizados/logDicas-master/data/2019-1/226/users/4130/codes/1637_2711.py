x = int(input("Valor disponivel: "))
x1 = int(input("Tickets que quer comprar: "))
x2 = float(input("Valor dos tickets: "))
x3 = int(input("Quantidade de passes do onibus: "))
x4 = float(input("Valor dos passes: "))

total = x - ((x1 * x2) + (x3 * x4)) 

if(total > 0):
	mensagem = "suficiente".upper()
if(total < 0):
	mensagem = "insuficiente".upper()
	
print(mensagem)