# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

vi = float(input("Valor da vel. inicial: "))
ang = radians(float(input("Valor do angulo: ")))
d = float(input("Valor da distancia horizontal: "))
g = 9.8

r = (( (vi**2) * ( sin(2*ang) ) )/g)

if(abs(d - r) <= 0.1):
	print("sim")
else:
	print("nao")
