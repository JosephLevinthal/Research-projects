j=float(input("valor de x:"))
if(j==-2) or (j==2) or (j< -1000) or (j < 1000):
	print("entrada invalida:")
	
else:
	if(j >= -1000) and (j < -2):
		valor=-((1) / (j+2))
		print(round(valor,4))
		
	elif(j < 2) and (j <= 1000):
	   valor=((1) / (j-2))
	   print(round(valor,4))
	
