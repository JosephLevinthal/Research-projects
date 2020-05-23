val=float(input("valor:"))
quant=int(input("quantidade de tickets:"))
valt=float(input("valor do ticket:"))
quantp=int(input("quantidade de passes:"))
valp=float(input("valor do passe:"))
x= val - quant * valt - quantp * valp
if x>0:
	print("suficiente".upper())
else:
	print("insuficiente".upper())