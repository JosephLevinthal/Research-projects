c= float(input("consumo: "))
if(c==0.0):
	print(round(c+30.00, 2))
else:
	if	(c<10):
		print(round(c*3.00+30.0, 2))
	else:
		print(round(c*3.50+30.0, 2))
