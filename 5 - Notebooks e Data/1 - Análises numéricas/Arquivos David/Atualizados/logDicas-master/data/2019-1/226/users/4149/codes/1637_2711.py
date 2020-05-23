valcart=float(input("entre com o valor  disponivel: "))
quanttick=int(input("entre com a quantidade de tickets: "))
valortick=float(input("entre com o valor do ticket: "))
quantpass=int(input("entre com a quantidade de passes: "))
valorpass=float(input("entre com o valor do passe: "))


if((quanttick*valortick)+(valorpass*quantpass)>valcart):
	
	print("INSUFICIENTE")
	
else:
	print("SUFICIENTE")
	