# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
import math
vo=float(input("Velocidade inicial: "))
a=float(input("Angulo do vetor: "))
D=float(input("Distancia: "))

R=(vo**2)*math.sin(math.radians(2*a))/9.8

if abs(D-R < 0.1):
	print("sim")
else:
	print("nao")