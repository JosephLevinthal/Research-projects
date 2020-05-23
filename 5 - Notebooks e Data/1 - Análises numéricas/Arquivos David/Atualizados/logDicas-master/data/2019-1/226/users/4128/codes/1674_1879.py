# Ao testar sua solução, não se limite ao caso de exemplo.
e = float(input("numero de horas extras:"))
f = float(input("numero de faltas: "))

h = e-(1/4*f) 
z = round(h,2)
print(e,"extras e",f,"de falta")

if(z > 400):
	print("R$ 500.0")
else:
	print("R$ 100.0")
	
	