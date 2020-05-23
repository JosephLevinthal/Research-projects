# Ao testar sua solução, não se limite ao caso de exemplo.
ext = float(input("Horas extras: "))
fal = float(input("Horas que faltou: "))

H = ext - (1/4)*fal

if(H > 400):
	print(ext,"extras e",fal,"de falta")
	print("R$",round(500.00, 2))
elif(H <=400):
	print(ext,"extras e",fal,"de falta")
	print("R$",round(100.00, 2))