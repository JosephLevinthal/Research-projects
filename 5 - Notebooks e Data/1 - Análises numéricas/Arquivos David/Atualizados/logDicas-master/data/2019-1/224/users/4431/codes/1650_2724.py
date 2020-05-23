x=int(input("Digite um numero: "))
y=int(input("Digite um numero:"))
z=int(input("Digite um numero: "))
if(x>y>z or z>y>x):
   print(y)
else:
	if(z>x>y or y>x>z):
	   print(x)
	else:
		print(z)