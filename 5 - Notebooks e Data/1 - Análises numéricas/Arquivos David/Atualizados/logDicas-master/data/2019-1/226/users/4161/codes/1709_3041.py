x = float(input("valor de x: "))

if not(-1000<=x<-2) and not(2<x<=1000):
	print("entrada invalida")
elif (-1000<=x<2):
	fx = -(1/(x+2))
	print(round(fx,4))
elif (2<x<=1000):
	fx = 1/(x-2)
	print(round(fx, 4))
