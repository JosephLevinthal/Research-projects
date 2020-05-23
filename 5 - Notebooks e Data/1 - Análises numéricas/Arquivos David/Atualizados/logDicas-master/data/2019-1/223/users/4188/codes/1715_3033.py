n=float(input("valor de x: "))
if(n>=-100 and n<0):
	fx=(-(1/n))
	print(round(fx,4))
if(n>0 and n<=100):
	fx=(1/n)
	print(round(fx,4))
if(n<-100 or n>100):
	print("entrada invalida")