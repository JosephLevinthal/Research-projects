j = float(input("digite taxa: "))
valor = float(input("digite valor: "))
Qo= 1500
t = 36

Qf = Qo * (1 + j) ** t 

if (valor <= Qf):
	msg = Qf
	print(round(Qf, 2))
	print("Sim")
else: 
	msg = Qf
	print(round(Qf, 2))
	print("Nao")