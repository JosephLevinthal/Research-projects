n = int(input("Numero de 3 digitos: "))

divisor = n % 100

if(n % divisor == 0):
	print("SIM")
else:
	print("NAO")