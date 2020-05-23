# Entradas
Tar = float(input("Temperatura: "))
v = float(input("Velocidade: "))
# Condicoes: validacao das entradas
if (Tar < -50) or (Tar > 10):
	print("Temperatura invalida")
elif (v <= 4.8):
	print("Velocidade invalida")
else:
	s = (13.12 + 0.6215 * Tar - (11.37 * v ** 0.16) + (0.3965 * Tar * v ** 0.16))
	print(round(s, 4))
	