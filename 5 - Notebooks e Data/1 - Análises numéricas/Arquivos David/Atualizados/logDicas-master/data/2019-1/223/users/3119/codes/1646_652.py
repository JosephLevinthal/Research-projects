num = int(input("Digite os numeros: "))
resto = num % 100

if(num % resto == 0):
	print("SIM")
else:
	print("NAO")