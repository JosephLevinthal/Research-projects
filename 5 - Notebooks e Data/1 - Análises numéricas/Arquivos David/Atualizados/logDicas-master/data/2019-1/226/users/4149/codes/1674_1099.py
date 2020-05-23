a=float(input("ladoa "))
b=float(input("lado b "))
c=float(input("ladoc "))
t= "Tipo de triangulo:"
print("Entradas:",a,",",b,",",c)
if(a<0)and(b<0)and(c<0):
	print(t,"invalido")
elif((a+b<=c)or(a+c<=b)or(b+c<=a)):
	print(t,"invalido")
elif((a==b)and(b==c)):
	print(t,"equilatero")
elif((a==b)or(b==c)or(c==a)):
	print(t,"isosceles")
elif((a!=b)and(a!=c)and(b!=c)):
	print(t,"escaleno")
			