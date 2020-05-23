a=float(input("Digite a: "))
b=float(input("Digite b: "))
c=float(input("Digite c: "))
d=float(input("Digite d: "))
e=float(input("Digite e: "))
f=float(input("Digite f: "))
g=a*e-b*d

if(g==0):
	print("Nao tem solucao")
if(g!=0):
	x=(c*e-b*f)/(a*e-b*d)
	y=(a*f-c*d)/(a*e-b*d)
	print(x)	
	print(y)


	