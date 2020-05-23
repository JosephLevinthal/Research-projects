#Entradas

escala = input("Celsius (C) ou Fahrenheit (F)? ")
temp = float(input("Qual o valar da temperatura? "))

if(escala == "C"):
	m = (1.8 * temp) + 32
if(escala == "F"):
	m = 5/9 * (temp - 32)

print(round(m,2))