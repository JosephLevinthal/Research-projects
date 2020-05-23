nota= float(input("valor"))
bon = input("S/N")
var = (nota*10)/100

if(bon.upper() == "S"):
	print(nota + var)
else:
	print(nota)



