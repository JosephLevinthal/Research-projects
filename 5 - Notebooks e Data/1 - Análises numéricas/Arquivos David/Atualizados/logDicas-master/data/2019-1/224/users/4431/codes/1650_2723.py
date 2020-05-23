x=int(input("Digite um numero: "))
y=int(input("Digite um numero:"))
z=int(input("Digite um numero: "))
if(x>y>z or x>z>y):
   print(x)
else:
	if(z>x>y or z>y>x):
	   print(z)
	else:
		print(y)