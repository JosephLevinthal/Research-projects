valor = int(input("Valor disponivel: "))
tick_q = int(input("Quantidade de tickets: "))
tick_v = float(input("Valor dos tickets: "))
passe_q = int(input("Quantidade de passes: "))
passe_v = float(input("Valor do passe: "))

if(valor >= (tick_q*tick_v)+(passe_q*passe_v)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")