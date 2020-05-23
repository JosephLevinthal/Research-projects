# Ao testar sua solução, não se limite ao caso de exemplo.
e = float(input("horas extras: "))
f = float(input("horas de falta: "))

print(e,"extras e", f,"de falta")

h = e - ((1/4) * f)
if (h > 400.00):
	l = 500.00
else:
	l =100.00
print("R$",round(l ,2))