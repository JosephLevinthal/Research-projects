n = int(input("numero de tres digitos: "))
nr = n%100

if( n % nr == 0):
	print("SIM")
else:
	print("NAO")