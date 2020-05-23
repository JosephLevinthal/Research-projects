x=float(input("valor disponivel: "))
y=int(input("quantidade de tickets: "))
z=float(input("valor do tickets: "))
w=int(input("passes de onibus: "))
t=float(input("valor dos passes: "))

if((y*z) + (w*t)< x):
	mensagem="SUFICIENTE"
else:
	mensagem="INSUFICIENTE"
	
print(mensagem)
