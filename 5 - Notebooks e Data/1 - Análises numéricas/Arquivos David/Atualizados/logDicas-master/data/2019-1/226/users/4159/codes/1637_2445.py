esc = input("escala: ").upper()
temp = float(input("temperatura: "))
if(esc=="C"):
	f= temp*9/5+32
	print(round(f, 2))
else:
	c = 5/9*(temp-32)
	print(round(c, 2))
