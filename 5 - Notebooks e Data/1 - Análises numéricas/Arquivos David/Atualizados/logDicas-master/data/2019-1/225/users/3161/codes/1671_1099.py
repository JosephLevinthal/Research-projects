a=float(input("lado A: "))
b=float(input("lado B: "))
c=float(input("lado C: "))

print("Entradas: ",a,", ",b,", ",c)

if a<=0 or b<=0 or c<=0:
   print("Tipo de triangulo: invalido")
	
elif a+b<=c or b+c<=a or a+c<=b:
	print("Tipo de triangulo: invalido")
	
elif a==b and b==c and a==c:
   print("Tipo de triangulo: equilatero")

elif a==b or b==c or c==a:
   print("Tipo de triangulo: isosceles")

elif a!=b and b!=c and a!=c:
	print("Tipo de triangulo: escaleno")
	


