saldo = float(input("valor disponivel:"))
ru = int(input("quantidade de tickets do RU:"))
vru = float(input("valor do ticket do RU:"))
qpasses = int(input("quantidade de passes:"))
vpasse = float(input("valor do passe:"))

x = ((vru*ru)+(vpasse*qpasses))

if (saldo > x):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")