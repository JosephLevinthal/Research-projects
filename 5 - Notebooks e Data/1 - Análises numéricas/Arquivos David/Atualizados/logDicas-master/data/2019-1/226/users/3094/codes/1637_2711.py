valor = float(input("valor: "))
qru = int(input("RU: "))
vru = float(input("valor RU: "))
qb = int(input("busao: "))
vb = float(input("valor busao: "))
f = qru * vru + qb * vb
if (valor >= f):
	saldo = "SUFICIENTE"
else: 
	saldo = "INSUFICIENTE"
print(saldo)