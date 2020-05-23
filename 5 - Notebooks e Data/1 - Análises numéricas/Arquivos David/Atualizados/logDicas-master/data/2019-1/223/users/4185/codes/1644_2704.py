nota= float(input("digite a nota"))
boni= input("S/N")

bonii= (nota*10)/100

if (boni == "S"):
	print(nota + bonii)
	
else:
	print(nota)