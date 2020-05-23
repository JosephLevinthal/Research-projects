x=float(input("digite x: "))

if( -1000<=x<-2):
	fx= - 1/ (x + 2)
	print(round(fx, 4))
elif(2<x<=1000):
	fx=1/ (x-2)
	print(round(fx, 4))
else:
	print("entrada invalida")