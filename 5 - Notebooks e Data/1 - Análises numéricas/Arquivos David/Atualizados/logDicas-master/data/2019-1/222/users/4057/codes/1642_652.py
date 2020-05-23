n = int(input("leia um numero de 3 digitos: "))

a = n // 100
a1 = n % 100

if (n%a1) == 0 :
	print("SIM")
else: 
	print("NAO")