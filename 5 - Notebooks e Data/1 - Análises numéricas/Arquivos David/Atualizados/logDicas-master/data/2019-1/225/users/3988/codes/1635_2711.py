v = float(input("valor:"))
q1 = int(input("quantidade:"))
v1 = float(input("valor1:"))
q2 = int(input("quantidade1:"))
v2 = float(input("valor2:"))
var = float((q1 * v1) + (v2 * q2))
if (v>=var):
	m = "SUFICIENTE"
else:
	m = "INSUFICIENTE"
print(m)	