x0 = float(input("Insira as coodenadas: "))
y0 = float(input("Insira as coodenadas: "))
x1 = float(input("Insira as coodenadas: "))
y1 = float(input("Insira as coodenadas: "))
x2 = float(input("Insira as coodenadas: "))
y2 = float(input("Insira as coodenadas: "))

c = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if(c < 0):
	p2 = "A direita da reta"
elif(c > 0):
	p2 = "A esquerda da reta"
elif(c == 0):
	p2 = "Sobre a reta"
print(p2)