x = float(input("Digite um numero referente a x:"))
if(x<=1):
	print(1)
elif((1<x)and(x<=2)):
	print(2)
elif((2<x)and(x<=3)):
	print(round (x**2,2))
else:
	print(round (x**3,2))