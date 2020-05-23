e = input("Escala em que a temperatura esta presente: ")
v = float(input("Valor da temperatura: "))

if (e == "C"):
	f = ((9*v)/5)+32
	print(round(f,2))
else:
	c = 5/9*(v-32)
	print(round(c,2))