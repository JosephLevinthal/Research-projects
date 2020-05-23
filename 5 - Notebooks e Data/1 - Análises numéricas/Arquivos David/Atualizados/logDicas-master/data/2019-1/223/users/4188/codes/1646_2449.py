a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
d=float(input("d: "))
e=float(input("e: "))
f=float(input("f: "))
m=(a*e - b*d)
if(m==0):
	print("Nao tem solucao")
if(m!=0):
	x=(c*e - b*f)/m
	y=(a*f - c*d)/m
	print(x)
	print(y)