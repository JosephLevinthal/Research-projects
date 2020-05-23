s = float(input("valor:"))
q = int(input("quantidade de tickets do RU:"))
vt= float(input("valor dos tickets:"))
qp= int(input("quantidade de passe de onibus:"))
vp= float(input("valor dos passe:"))

a = (q * vt) + (qp * vp)
if (a < s):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")