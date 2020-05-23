a=float(input("coloca o a mano "))
b=float(input("coloca o b mano "))
c=float(input("coloca o c mano "))
d=float(input("coloca o c mano "))
e=float(input("coloca o e mano "))
f=float(input("coloca o f mano "))

if((a*e)-(b*d)==0):
	
	print("Nao tem solucao")
	
else:
	x=((c*e)-(b*f))/((a*e)-(b*d))
	y=((a*f)-(c*d))/((a*e)-(b*d))
	
	print(x)
	print(y)
	
	
