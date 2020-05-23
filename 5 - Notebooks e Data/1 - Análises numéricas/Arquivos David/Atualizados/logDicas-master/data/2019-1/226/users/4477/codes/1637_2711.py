valor = int(input("Determine o valor: "))
qdt = int(input("Determine a quantidade: "))
vt = float(input("Valor dos tickets: "))
qpo = int(input("Determine a quantidade de passes: "))
vdp = float(input("Valor dos passes: "))

x = (qdt * vt) + (qpo * vdp)

if (valor >= x):
	msg = "SUFICIENTE"
else:
	msg = "INSUFICIENTE"
print(msg)