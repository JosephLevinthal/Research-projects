from math import*
x = float(input("funcao (x):"))

if ((x >= -4) and (x < 0)):
	fx = abs(x) ** (1/2)
	print(round(fx , 4))
elif(abs(x == 0)):
	fx = 0
	print(fx)
elif((x > 0) and (x <= 4)):
	fx = x ** (1/2)
	print(round(fx , 4))
else:
	print("entrada invalida")
		