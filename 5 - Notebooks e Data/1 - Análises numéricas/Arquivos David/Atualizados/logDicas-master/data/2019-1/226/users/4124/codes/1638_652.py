n = int(input("Digite um numero de 3 digitos: "))

n1 = n // 100
r = n % 100
if(n % r == 0):
	print("SIM")
else:
	print("NAO")
