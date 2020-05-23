num = float(input("Digite um numero de 3 digitos:"))
num_rem = (num%100)
if (num%num_rem==0):
	print("sim".upper())
else:
	print("nao".upper())