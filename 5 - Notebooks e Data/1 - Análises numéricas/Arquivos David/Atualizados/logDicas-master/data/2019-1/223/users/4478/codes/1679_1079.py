A=float(input("valor de A: "))
B=float(input("valor de B: "))
C=float(input("valor de C: "))
print("Entradas:", A, ",", B, ",", C)
if((A>=B+C)or(B>=A+C)or(C>=A+B)):
	print("Area: invalida")
else:
	x=(A*B)/2
	area = round(x,3)
	print("Area:", area)

	
	