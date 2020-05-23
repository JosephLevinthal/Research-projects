x=float(input("Valor disponivel:"))
y=int(input("quantidade de tickets:"))
z=float(input("valor dos tickets:"))
w=int(input("quantidade de passses:"))
q=float(input("valor dos passes:"))
if((y*z)+(w*q)>x):
	print("INSUFICIENTE")
else:
	print("SUFICIENTE")