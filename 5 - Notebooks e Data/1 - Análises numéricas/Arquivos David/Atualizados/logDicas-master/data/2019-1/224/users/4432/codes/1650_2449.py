a=float(input("digite a:    "))
b=float(input("digite b:    "))
c=float(input("digite c:    "))
d=float(input("digite d:    "))
e=float(input("digite e:    "))
f=float(input("digite f:    "))
x=(c*e-b*f)
y=(f*a-c*d)
z=(a*e)-(b*d)
if(z==0):
	print("Nao tem solucao")
else:
	print(x/z)
	print(y/z)