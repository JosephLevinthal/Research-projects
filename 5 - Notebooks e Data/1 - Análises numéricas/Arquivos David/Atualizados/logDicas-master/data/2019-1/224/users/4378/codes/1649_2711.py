val=float(input("valor:"))
qtdtic=int(input("quantidade de tickets:"))
valtic=float(input("valor do ticket:"))
qtdbus=int(input("quantidade de passes:"))
valbus=float(input("valor do passe:"))
x= val -(qtdtic * valtic) - (qtdbus * valbus)
if x>0:
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")