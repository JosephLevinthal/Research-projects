a = float(input("numero: "))
b = float(input("numero: "))
c = float(input("numero: "))
print("Entradas:", a,",",b ,",", c)
if(a+b<=c)or(b+c<=a)or(c+a<=b):
	mensagem=("invalido")
elif(a==b)and(b==c)and(b==a):
	mensagem=("equilatero")
elif(a==b)or(a==c)or(b==c):
	mensagem=("isosceles")
else:
	mensagem=("escaleno")
print("Tipo de triangulo:", mensagem)