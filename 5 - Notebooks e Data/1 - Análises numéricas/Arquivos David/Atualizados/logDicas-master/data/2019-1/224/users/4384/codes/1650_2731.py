x=float(input("coeficiente  y    "))
y=float(input("coeficiente x   "))
r=float(input("raio   "))
if(x>0 and y>0):
	print("Superiores")
else:
	if(x>0 and y<0):
		print("Inferiores")
	else:
		if(x<0 and y<0):
			print("Inferiores")
		else:
			print("Superiores")