a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

if(a*e-b*d) !=0:
	x = (c*e-b*f)/(a*e-b*d)
	y = (a*f-c*d)/(a*e-b*d)
	print(x,y)
else:("Nao tem solucao")