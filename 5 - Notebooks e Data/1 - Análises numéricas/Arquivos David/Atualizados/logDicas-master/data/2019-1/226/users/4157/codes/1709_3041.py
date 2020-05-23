x = float(input("valor d x:"))
if(x >= -1000)and(x < -2) :
	f = (-1)/(x + 2)
	print(round(f, 4))
elif(x > 2)and(x<=1000):
	f = 1/(x-2)
	print(round(f, 4))
else:
	print("entrada invalida")