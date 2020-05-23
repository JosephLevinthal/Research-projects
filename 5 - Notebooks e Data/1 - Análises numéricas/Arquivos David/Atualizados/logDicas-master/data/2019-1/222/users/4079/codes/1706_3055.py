x=float(input("valor consumido:"))
if(x >= 0)and (x <= 100):
	gorjeta=0.1
	valor= x+x*0.1
	print(round(valor,2))
elif(x > 100) and (x <= 200):
	gorjeta=0.09
	valor=x+x*0.09
	print(round(valor,2))
elif(x > 200) and (x <= 300):
	gorjeta=0.08
	valor=x+x*0.08
	print(round(valor,2))
elif(x > 300):
	gorjeta=0.07
	valor=x+x*0.07
	print(round(valor,2))
else:	
	print(round(valor,2))