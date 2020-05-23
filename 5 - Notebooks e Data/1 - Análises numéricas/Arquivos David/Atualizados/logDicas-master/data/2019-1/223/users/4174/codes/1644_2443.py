from math import*

raio = float(input("valor do raio:"))
x = float(input("altura do ar em x:"))

opcao = int(input("volume do ar (1) ou volume do combustivel (2)"))
calota = pi/3 * x**2*(3 * raio - x)

if (opcao == 1):
	volume = calota
else:
	volume = 4/3 * pi * raio**3 - calota
print(round(volume, 4))