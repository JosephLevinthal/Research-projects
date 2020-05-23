a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
g=c*e-b*f
w=a*e-b*d
u=a*f-c*d
if((w)==0):
	print("Nao tem solucao")
else:
	x=g/w
	y=u/w
	print(x)
	print(y)
