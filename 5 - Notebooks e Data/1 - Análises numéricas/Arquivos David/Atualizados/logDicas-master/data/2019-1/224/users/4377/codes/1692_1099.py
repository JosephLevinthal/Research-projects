a=float(input("a"))
b=float(input("b"))
c=float(input("c"))

if(a>=b+c) or (b>=a+c) or (c>=b+a) or (a<0) or (b<0) or (c<0):
	merda=("invalido")
elif(a==b) and (b==c):
	merda="equilatero"
elif(a==b) or (b==c) or (c==a):
   merda="isosceles"
else:
	merda="escaleno"


print("Entradas:", a , "," , b , ",", c)
print("Tipo de triangulo:", merda)
    
     









