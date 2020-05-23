n = int(input("Digite um numero de tres digitos: "))
x = n % 100 
y = n % x

if(n % x == 0):
	resp = "SIM"
	print(resp)
else:
	resp = "NAO"
	print(resp)