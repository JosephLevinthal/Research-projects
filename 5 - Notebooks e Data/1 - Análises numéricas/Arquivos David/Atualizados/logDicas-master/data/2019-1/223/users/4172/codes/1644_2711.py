V=int(input("valor disponivel: "))
QRU=int(input("quanidadeda de tickets do ru: "))
VRU=float(input("valor dos tickets: "))
PO=int(input("passes de bus: "))
VP=float(input("valor do passe: "))
x=(QRU*VRU)
y=(PO*VP)
W=x+y
if V>W:
	mensafnjdfnkjnfvksagem="SUFICIENTE"
else:
	mensagem="INSUFICIENTE"
	
print(mensagem)