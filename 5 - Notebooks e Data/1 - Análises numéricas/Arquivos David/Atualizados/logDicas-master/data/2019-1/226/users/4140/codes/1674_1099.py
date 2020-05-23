a=float(input());
b=float(input());
c=float(input());
print("Entradas:", a, ",", b, ",", c)
if (a<=0 or b<=0 or c<=0 ):
	print("Tipo de triangulo: invalido");
else:
	if(a+b)>c and (a+c)>b and (b+c)>c:
		if(a==b and b==c):
			print("Tipo de triangulo: equilatero")
		else:
			if(a==b or b==c or a==c):
				print("Tipo de triangulo: isosceles");
			else:
				print("Tipo de triangulo: escaleno");
	else:
		print("Tipo de triangulo: invalido")
	

	
	
	
