esc = input("Escala da temperatura(C/F): ").upper()
val = float(input("Insira a temperatura: "))

if(esc == "F"):
	temp = (5/9) * (val - 32)
else:
	temp = (9 * val)/5 + 32
print(round(temp,2))
