t = input("temp em celsius c / F: ")
vt = float(input("valor da temp: "))
if (t == "F"):
	v = 5 / 9 * (vt - 32)
if (t == "C"):
	v = (vt *(9 / 5)) + 32
print(round(v , 2))