x=float(input("x: "))

if((x >= -1000) and (x<-2)):
	
	fx= (-1)*(1/(x+2))
	print(round(fx,4))
	
elif ((x>2) and (x<=1000)):
	
	fx=(1/(x-2))
	print(round(fx,4))
	
else:
	print("entrada invalida")
	

