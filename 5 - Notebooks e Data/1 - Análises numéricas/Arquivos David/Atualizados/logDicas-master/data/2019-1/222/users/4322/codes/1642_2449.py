a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
q=a*e-b*d
if (q==0):
	print("Nao tem solucao")

else:
	x=(c*e-b*f)/q
	y=(a*f-c*d)/q
	print(x)
	print(y)