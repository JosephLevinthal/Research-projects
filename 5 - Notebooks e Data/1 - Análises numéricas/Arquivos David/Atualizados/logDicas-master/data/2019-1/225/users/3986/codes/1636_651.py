a=float(input("altura em metros: "))
s=input("Sexo M/F: ")

if (s.upper()=="M"):
	h=(72.7 * a) - 58
	print(round(h, 2))
	
else :
	x=(62.1 * a) - 44.7
	print(round(x,2))