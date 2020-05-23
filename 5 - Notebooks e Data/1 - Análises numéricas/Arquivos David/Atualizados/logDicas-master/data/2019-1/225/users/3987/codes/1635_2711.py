disponivel = float(input("disponivel:"))
tickets = int(input("quantidade:"))
valor = float(input("preco:"))
passes = int(input("passes:"))
preco = float(input("valor:"))
c = (tickets * valor) + (passes * preco)
if (disponivel > c):
   print("SUFICIENTE")
else:
	print("INSUFICIENTE")
	