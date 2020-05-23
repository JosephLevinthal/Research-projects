valor = float(input("Digite um numero:"))
tick = int(input("Digite um numero:"))
ptick = float(input("Digite um numero:"))
ps = int(input("Digite um numero:"))
pps = float(input("Digite um numero:"))

rusbe = tick * ptick + ps * pps

if (valor >= rusbe):
	wpp = "SUFICIENTE"
else:
	wpp = "INSUFICIENTE"

print(wpp)

