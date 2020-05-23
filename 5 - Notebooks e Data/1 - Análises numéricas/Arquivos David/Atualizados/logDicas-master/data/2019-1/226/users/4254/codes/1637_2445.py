esc = input("Escala da temperatura em Celsius(C) ou Fahrenheit(F) ")
val = int(input("Valor da temperatura: "))

if(esc.upper() == "C"):
	f = ((9*val)/5) + 32
	print(round(f,2))
if(esc.upper() == "F"):
	c = 5/9*(val - 32)
	print(round(c,2))