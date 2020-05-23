vl = float(input("carteira vazia: "))
x = int(input("ru = vida: "))
y = float(input("pora tudo isso: "))
w = int(input("passe pro busao lotado: "))
z = float(input("passagem ta cara pra po*a: "))

if(vl >= (x * y) + (w * z)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")