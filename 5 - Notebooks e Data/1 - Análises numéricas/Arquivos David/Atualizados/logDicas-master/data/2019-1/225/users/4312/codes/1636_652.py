numero = int(input("Informe um numero de 3 digitos:\n"))
n = numero//100%10

if(numero%n == 0):
	print("SIM")
else:
	print("NAO")