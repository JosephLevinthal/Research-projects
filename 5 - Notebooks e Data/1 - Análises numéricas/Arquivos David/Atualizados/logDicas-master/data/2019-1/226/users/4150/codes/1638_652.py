a = int(input("digite o numero: "))

b = a//100
c = a%100
d = a%c

if ( d == 0  ):
	print("SIM")
else:
	print("NAO")