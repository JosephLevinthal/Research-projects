a=float(input("digite o numero:"))
b=float(input("digite o numero:"))
c=float(input("digite o numero:"))
if(a>=b+c) or (b>=a+c) or (c>=b+a) or (a<0) or (b<0) or (c<0):
	mensagem="invalido"
elif(a==b and b==c):
	mensagem="equilatero"
elif(a==b or b==c or a==c):
	mensagem="isosceles"
else:
	mensagem="escaleno"
	
	
print("Entradas:", a ,"," , b, "," , c)
print("Tipo de triangulo:", mensagem)

