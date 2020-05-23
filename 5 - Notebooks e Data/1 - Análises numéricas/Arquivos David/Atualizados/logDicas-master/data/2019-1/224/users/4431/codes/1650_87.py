x=int(input("Digite um numero: "))
y=int(input("Digite um numero:"))
z=int(input("Digite um numero: "))
if(x>y>z or y>x>z):
   print(z)
else:
	if(z>x>y or x>z>y):
	   print(y)
	else:
		print(x)
			
		
	
	