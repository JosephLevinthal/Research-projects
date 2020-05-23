# Entradas
E = float(input("Horas extras: "))
F = float(input("No. de faltas em horas: "))
# Saidas pt. 1
print(E, "extras e", F, "de falta")
# Condicoes
H = E - 1/4 * F
if(H <= 400):
	print("R$", round(100.00, 2))
else: 
	print("R$", round(500.00, 2))
