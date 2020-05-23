x=float(input("Quantidade inciail de virus: "))
y=float(input("Quantidade incial de leucocitos: "))
z=float(input("Percentual diaria do virus: "))
h=float(input("Percentual diario de leucocitos: "))
z=z/100
h=h/100
j=0
while(x>y/2):
	x=x+(x*z)
	y=y+(y*h)
	j=j+1
print(j)	
	