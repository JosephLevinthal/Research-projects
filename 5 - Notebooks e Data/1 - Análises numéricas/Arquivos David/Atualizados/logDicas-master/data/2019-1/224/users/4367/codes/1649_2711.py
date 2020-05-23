v=float(input("digite o valor disponivel: "))
ru=int(input("numero de tickets: "))
vlt=float(input("preco do tickets: "))
po=int(input("numero de passes: "))
vp=float(input("valor do passe: "))
x= (v-((ru*vlt)+(po*vp)))
if(x>=0):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")