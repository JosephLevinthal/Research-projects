from math import*
x=float(input("Digite o numero em graus "))
if(x<0)or(x>360):
	print("entrada invalida")
elif((x>=0)and(x<90))or((x>=180)and(x<270)):
	x=radians(x)
	z=sin(x)
	print(round(z,4))
elif((x>=90)and(x<180)or(x>=270)and(x<360)):
	x=radians(x)
	z=cos(x)
	print(round(z,4))