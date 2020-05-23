a=float(input("Digite o coeficiente a : "))
b=float(input("Digite o coeficiente b : "))
r=float(input("Digite o raio: "))
if(a>0 and b>0):
   print("Superiores")
else:
	if(a>0 and b<0):
		print("Inferiores")
	else:
		if(a<0 and b>0):
			print("Superiores")
		else:
			print("Inferiores")