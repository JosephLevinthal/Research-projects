a=float(input())
b=float(input())
c=float(input())

print("Entradas:", a ,"," , b ,"," , c)

if(a==b and b==c) :
		  print("Tipo de triangulo: equilatero")
elif (a==b or b==c or c==a ) :
		  print("Tipo de triangulo: isosceles")
elif((a>=b+c or b>=c+a or c>=a+b) or (a<=0 or b<=0 or c<=0)):
		  print("Tipo de triangulo: invalido")
else:
		  print("Tipo de triangulo: escaleno")