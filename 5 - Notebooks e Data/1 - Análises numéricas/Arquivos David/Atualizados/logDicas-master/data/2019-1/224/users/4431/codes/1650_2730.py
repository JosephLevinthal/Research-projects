x=float(input("Digite a coordenada x : "))
y=float(input("Digite a coordenada y : "))
if(x>0 and y>0):
   print("Superiores")
else:
	if(x>0 and y<0):
		print("Inferiores")
	else:
		if(x<0 and y>0):
			print("Superiores")
		else:
			print("Inferiores")