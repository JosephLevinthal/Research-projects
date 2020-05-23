a = float(input("altura: "))
b = input("sexo: ").upper()
if( b == "M"):
	c = (72.7*a)-58
else:
	c = (62.1*a)-44.7
print(round(c,2))