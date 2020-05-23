a=float(input("numeros "))
cont=0
conte=0
while(a!=0):
	if(a%2==0):
		cont=cont+1
		a=float(input("nu"))	
	else:
		conte=conte+1
		a=float(input("numeross"))
x=cont+conte
z=(cont/x)*100
y=(conte/x)*100
print(round(z,2))
print(round(y,2))