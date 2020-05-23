a=float(input("c1: "))
b=float(input("c2: "))
c=float(input("c3: "))
d=float(input("c4: "))
e=float(input("c5: "))
f=float(input("c6: "))
x=(c*e-b*f)/(a*e-b*d)
y=(a*f-c*d)/(a*e-b*d)
if(a*e-b*d!=0):
	print(x)
	print(y)
else:
	print("Nao tem solucao")