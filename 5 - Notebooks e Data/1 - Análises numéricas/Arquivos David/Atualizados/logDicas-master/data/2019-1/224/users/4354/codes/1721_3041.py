x = float(input("digite x: "))


if(-1000<=x<-2 and x !=-2):
	y = -(1/(x+2))
	print(round(y,4))
elif(2<x<=1000 and x != 2):
	y = (1/(x-2))
	print(round(y,4))
else:
	print("entrada invalida")