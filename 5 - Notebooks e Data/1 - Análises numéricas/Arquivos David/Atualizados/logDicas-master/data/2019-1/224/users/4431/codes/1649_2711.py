x=float(input("Digite o valor disponivel: "))
y=int(input("Digite a quantidade de tickets: "))
z=float(input("Digite o valor dos ticktes: "))
a=int(input("Digite a quantidade de passes: "))
b=float(input("Digite o valor dos passes: "))
if(x>=(y*z)+(a*b)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")