x=int(input("numero de 3 digitos:    "))
y=x//100
z=x%100
if(z%y==0):
	print("SIM")
else:
	print("NAO")
