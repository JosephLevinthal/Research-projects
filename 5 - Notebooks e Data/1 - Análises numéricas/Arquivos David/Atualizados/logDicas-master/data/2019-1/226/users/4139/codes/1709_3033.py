x = float(input("valor de x:"))

if(x<0)and(x>-100):
	y=-1/x
	print(round(y,4))
elif(0<x)and(x<100):
	y=1/x
	print(round(y,4))
else:
	print("entrada invalida")