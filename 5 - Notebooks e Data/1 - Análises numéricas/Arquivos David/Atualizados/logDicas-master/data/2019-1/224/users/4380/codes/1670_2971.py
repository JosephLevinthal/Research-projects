j=float(input("juros: "))
ap=float(input("valor do apartamento: "))
t=36
final=1500*((1+j)**t)
if (ap>final):
	print(float(round(final,2)))
	print("Nao")
else:
	print(float(round(final,2)))
	print("Sim")
	
