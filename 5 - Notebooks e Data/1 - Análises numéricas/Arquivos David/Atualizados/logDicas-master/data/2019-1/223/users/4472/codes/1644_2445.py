opcao = input("Escolha a escala: C- Celsius | F- Fahrenheit: ")
temperatura = float(input("Informe a temperatura: "))

if opcao == "C":
	f = (9 * temperatura) / 5 + 32
	print (round(f,2))
else:
	c = (5 / 9) * (temperatura - 32)
	print (round(c,2))
