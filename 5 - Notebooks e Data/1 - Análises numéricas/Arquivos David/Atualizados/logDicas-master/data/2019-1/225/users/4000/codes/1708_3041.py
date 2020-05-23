x = float(input("Valor de x: "))
if(x>=-1000 and x<-2):
	z = -1/(x+2)
	print(round(z, 4))
	
elif(x>2 and x<=1000):
	z = 1/(x-2)
	print(round(z, 4))
else:
	print('entrada invalida')



			 