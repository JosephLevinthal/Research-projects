a = float(input("a:"))
b = float(input("b:"))
c = float(input("x:"))
d = float(input("d:"))
e = float(input("e:"))
f = float(input("f:"))
x = (c*e-b*f)/(a*e-b*d)
y = (a*f-c*d)/(a*e-b*d)

if((c*e-b*f)/(a*e-b*d),(a*f-c*d/a*e-b*d)>0):
	print(x)
	print(y)
else:
	print("Nao tem solucao")
	