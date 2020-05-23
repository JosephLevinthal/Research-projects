x = float(input("digite x: "))

if(x<0)and(x>-100):
	fx= -1/x
	print(round(fx,4))
elif(x>0)and(x<=100):
	fx = 1/x
	print(round(fx,4))
else:
	print("entrada invalida")