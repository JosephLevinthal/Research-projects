ca = float(input("Digite o coeficiente a: "))
cb = float(input("Digite o coeficiente b: "))
r = float(input("Digite o raio: "))

if(ca > 0 and cb > 0):
	print("Superiores")
elif(ca < 0 and cb > 0):
	print("Superiores")
elif(ca > 0 and cb < 0):
	print("Inferiores")
else:
	print("Inferiores")

