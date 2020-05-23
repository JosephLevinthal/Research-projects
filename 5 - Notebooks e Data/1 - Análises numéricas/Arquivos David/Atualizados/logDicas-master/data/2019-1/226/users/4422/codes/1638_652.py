n = int(input("Digite o numero: "))
d1 = (n//100)*100

if(n % (n - d1) == 0):
	print("SIM")
	
else:
	print("NAO")