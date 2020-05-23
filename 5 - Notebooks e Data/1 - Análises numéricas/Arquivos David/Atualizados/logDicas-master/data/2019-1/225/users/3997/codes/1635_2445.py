esc = input("escala?: (C/F)")
temp = float(input(""))

if (esc == "C"):
	print(9* temp/5 + 32)
else:
	print(5/9 *(temp - 32))