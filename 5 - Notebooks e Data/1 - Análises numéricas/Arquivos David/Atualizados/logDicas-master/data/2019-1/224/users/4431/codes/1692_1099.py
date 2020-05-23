x=float(input("Digite o lado a: "))
y=float(input("Digite o lado b: "))
z=float(input("Digite o lado c: "))
print("Entradas:",x,",",y,",",z)
if((x>=y+z)or(y>=z+x)or(z>=y+x))or((x<0)or(y<0)or(z<0)):
	print("Tipo de triangulo: invalido")
else:
   if((x==y)and(y==z)):
	   print("Tipo de triangulo: equilatero")
   elif(y==x)or(x==z)or(y==z):
		   print("Tipo de triangulo: isosceles")
   else:
	     print("Tipo de triangulo: escaleno")	
				