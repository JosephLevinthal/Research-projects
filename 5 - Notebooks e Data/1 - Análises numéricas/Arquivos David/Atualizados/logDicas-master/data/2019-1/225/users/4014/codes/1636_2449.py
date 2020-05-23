a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
d=float(input("e:"))
f=float(input("f:"))
x=((c*e)-(b*f))/((a*e)-(b*d))
y=((a*f)-(c*d))/((a*e)-(b*d))
if((a*e)-(b*d)==0):
	msg="Nao tem solucao "
	print(msg)
else:
	print(x)
	print(y)