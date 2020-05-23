P = float(input("Percurso: "))
tipo = input("Tipo (A/B)? ")

cA = P / 8
cB = P / 12

if(tipo == "A"):
	msg = cA
else:
	msg = cB
print(round(msg, 2))