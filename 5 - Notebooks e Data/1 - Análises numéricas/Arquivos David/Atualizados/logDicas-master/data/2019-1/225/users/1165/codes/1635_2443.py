from math import*
raio = float(input("Raio do tanque: "))
x = float(input("Altura do ar: "))

opcao = int(input("Volume do ar (1) ou do liquido (2): "))
calota = pi/3 * x**2 * (3 * raio - x)

if (opcao == 1):
	volume = calota
else:
	volume = 4/3 * pi * raio**3 - calota

print(round(volume, 4))