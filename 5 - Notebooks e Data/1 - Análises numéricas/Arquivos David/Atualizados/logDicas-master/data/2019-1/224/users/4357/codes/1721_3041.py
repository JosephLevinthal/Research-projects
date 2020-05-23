x=float(input("digite o numero:"))
if(x>=-1000 and x<-2):
	f=round(-(1/(x+2)),4)
	print(f)
elif(x>2 and x<=1000):
	f=round((1/(x-2)),4)
	print(f)
else:
	print("entrada invalida")