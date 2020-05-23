a=float(input("valor de a: "))
b=float(input("valor de b: "))
c=float(input("valor de c: "))
d=float(input("valor de d: "))
e=float(input("valor de e: "))
f=float(input("valor de f: "))

p1=(a/d)
p2=(b/e)

if (p1 != p2):
	
	x=((c*e)-(b*f))/((a*e)-(b*d))
	y=((a*f)-(c*d))/((a*e)-(b*d))	
	print(x)
	print(y)	
	
else:
	print("Nao tem solucao")
	