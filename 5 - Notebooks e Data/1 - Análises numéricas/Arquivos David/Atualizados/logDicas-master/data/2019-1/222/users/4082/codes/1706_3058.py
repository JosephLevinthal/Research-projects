a=float(input("area:"))

if(a >= 0 and a <= 100):
	valor = a* 2+ 100
	
elif (a >= 10 and a <= 250):
	valor = a * 1.80+ 150
	
elif(a>=100 and a <= 2500):
	valor= a * 1.50 + 200
	
elif (a >= 2500 and a <= 10000 ):
	valor = a* 1.50+250
	
else:
	valor = a*1.20+250
print(round(valor,  2))


