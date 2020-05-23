valor = float(input("digite valor: "))
qt = int(input("digite qt: "))
vt = float(input("digite vt: "))
qp = int(input("digite qp: "))
vp = float(input("digite vp: "))

a = qt * vt + qp * vp 

if (a <= valor):
	print("SUFICIENTE")
else:
	a > valor
	print("INSUFICIENTE")