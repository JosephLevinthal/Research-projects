# Area fertilizada de 10.000 =< R$ 5,00
# area fertilizada for mais de 10.000> então pros 10.000 é 5 pro resto é 4
a = float(input("Area a ser fertilizada:"))

if (a <= 10000):
	eq = a * 5
	print(round(eq,2))
else:
	eq2 = a - 10000
	eq1 = (10000 * 5) + (eq2 * 4) 
	
	print(round(eq1,2))