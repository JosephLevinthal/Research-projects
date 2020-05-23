a=float(input("valor de a:"))
b=float(input("valor de b:"))
c=float(input("valor de c:"))
d=float(input("valor de d:"))
e=float(input("valor de e:"))
f=float(input("valor de f:"))

p=(a*e-b*d)

if(p==0):
	print("Nao tem solucao")
	
else:
	X=(c*e-b*f)/p
	Y=(a*f-c*d)/p
	print(X)
	print(Y)
