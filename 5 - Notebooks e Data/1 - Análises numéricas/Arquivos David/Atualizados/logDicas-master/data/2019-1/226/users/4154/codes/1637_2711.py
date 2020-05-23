a = int(input("valor disponivel: "))
b = int(input("tickets: "))
c = float(input("valor tickets: "))
d = int(input("passes: "))
e = float(input("valor do passe: "))

if (b*c + d*e)<a:
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")