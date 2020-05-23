esc = input("digite a escala desejada: ")
temp = float(input("digite a temperatura: "))

if (esc.upper() == "F"):
	conv = (5/9) * (temp - 32)
	
if (esc.upper() == "C"):
	conv = (temp / (5/9)) + 32
	
print(round(conv,2))
	
	