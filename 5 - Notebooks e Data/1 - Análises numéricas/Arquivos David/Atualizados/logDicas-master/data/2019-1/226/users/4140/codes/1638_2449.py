a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

numeradorx=(c*e-b*f)
denominadorx=(a*e-b*d)
numeradory=(a*f-c*d)
if(denominadorx==0 ):
	print("Nao tem solucao")
else :
	x=(numeradorx/denominadorx)
	y=(numeradory/denominadorx)
	print(x)
	print(y)