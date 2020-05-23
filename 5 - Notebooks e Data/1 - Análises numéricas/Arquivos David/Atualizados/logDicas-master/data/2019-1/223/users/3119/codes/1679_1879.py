# Ao testar sua solução, não se limite ao caso de exemplo.

e = float(input("Numero de horas extras: "))
f = float(input("Faltas (em horas): "))
print(e,"extras e",f,"de falta")
h = e - 1/4 * f

if(h > 400):
	print("R$ 500.0")
elif(h < 400):
	print("R$ 100.0")