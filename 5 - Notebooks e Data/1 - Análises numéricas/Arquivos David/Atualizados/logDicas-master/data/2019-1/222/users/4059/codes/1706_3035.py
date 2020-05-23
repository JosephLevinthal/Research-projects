import math 
x=float(input())
y=math.radians(x)


if (x<0 or x>360):
	print('entrada invalida')
elif ((x>=0 and x<90) or (x<=180 and x<270)):
	print(round(math.sin(y),4))
elif ((x>=90 and x<180) or (x>=270 or x<360)):
	print(round(math.cos(y),4))