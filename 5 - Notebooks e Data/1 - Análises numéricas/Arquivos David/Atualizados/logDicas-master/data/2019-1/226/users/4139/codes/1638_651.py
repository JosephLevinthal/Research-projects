a = float(input("altura:"))
s = (input("sexo M ou F:").upper())

h = (72.7*a)-58
m = (62.1*a)-44.7

if(s == "M"):
	print(round(h,2))
else:
	print(round(m,2))