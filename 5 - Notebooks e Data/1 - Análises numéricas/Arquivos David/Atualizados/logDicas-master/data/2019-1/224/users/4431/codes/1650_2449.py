a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))
d=float(input("Digite o valor de d: "))
e=float(input("Digite o valor de e: "))
f=float(input("Digite o valor de f: "))
x=(c*e)-(b*f)
y=(a*f)-(c*d)
z=(a*e)-(b*d)
if(z!=0):
	x=x/z
	y=y/z
	print(x)
	print(y)
else:
	print("Nao tem solucao")	
	