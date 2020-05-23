x=float(input("consumo de agua: "))

if(x<10):
	print(round(30+3*x,2))
else:
	print(round(30+(3.5*x),2))