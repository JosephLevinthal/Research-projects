x=float(input())

if(x>=-1000 and x<-2 ):
	valor=-1/(x+2)
	print(round(valor,4))
elif(x>2 and x<=1000):
	valor=1/(x-2)
	print(round(valor,4))
else:
	print("entrada invalida")