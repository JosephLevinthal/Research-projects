escala = input("Escala? (C/F)")
temp = float(input(""))

if (escala == "C"):
	print (9 * temp/5 + 32)
else:
	print (5/9 * (temp - 32))

