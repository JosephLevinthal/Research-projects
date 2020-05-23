a=float(input("lado a :"))
b=float(input("lado b :"))
c=float(input("lado c :"))
print("Entradas:" , a,",",b,",",c)
if ((a>=b+c)or(b>=a+c)or(c>=a+b)):
   print("Tipo de triangulo: invalido")
else:
   if((a==b)and(a==c)):
      print("Tipo de triangulo: equilatero")
   else:
      if((a == b)or(b == c)or(c == a)):
         print("Tipo de triangulo: isosceles")
      else:
         print("Tipo de triangulo: escaleno")
			 
			 