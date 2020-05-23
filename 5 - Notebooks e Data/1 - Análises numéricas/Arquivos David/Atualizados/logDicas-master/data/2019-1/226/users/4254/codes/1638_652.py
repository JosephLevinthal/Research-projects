n = int(input("Digite o numero: "))
nd = n //10 % 10
nu = n % 10
ndesc = nd*10 + nu
if(n % ndesc == 0):
	print("SIM")
else:
	print("NAO")