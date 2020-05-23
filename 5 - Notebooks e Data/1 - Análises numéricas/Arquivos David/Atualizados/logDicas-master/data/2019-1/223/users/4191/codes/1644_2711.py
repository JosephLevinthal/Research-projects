#v = valor que ele tem disponivel / qt = quantidade de tickets / vt = valor dos tickets /
#qp = quantidade de passes / vp = valor dos passes
v = int(input("Qual seu valor disponivel?:  "))
qt = int(input("Quantos tickets voce possui?: "))
vt = float(input("Quanl o valor dos tickets?: "))
qp = int(input("Quantos passes de onibus voce possui?: "))
vp = float(input("Qual o valor dos passes?: "))
if (v - (qt * vt + qp * vp) >= 0):
	m= "SUFICIENTE"
else:
	m= "INSUFICIENTE"
print(m)	