# Modulo numpy
from numpy import *
# Entrda
dano = array(eval(input("Determine os danos: ")))
# Variavel
i = 0
peso = 0
dt = 0
# Laço
while (i<size(dano)):
	if (i == 0):
		dt = dt + (dano * peso)
	i = i + 1
	peso = peso + 1

if (i > 0):
	dt = dt + (dano * peso)
# Saida
print(sum(dt))