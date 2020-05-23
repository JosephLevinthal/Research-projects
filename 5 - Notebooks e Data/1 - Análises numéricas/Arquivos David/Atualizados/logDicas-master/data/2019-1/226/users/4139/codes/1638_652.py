a = int(input("numero de 3 digitos:"))

x = a//100
y = a%100

if(a%y == 0):
	print("SIM")
else:
	print("NAO")