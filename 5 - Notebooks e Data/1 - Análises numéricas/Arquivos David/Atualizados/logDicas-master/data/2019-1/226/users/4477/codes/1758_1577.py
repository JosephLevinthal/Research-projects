# Modulo
from numpy import *
# Entradas
a = float(input("Determine a: "))
v0 = float(input("Determine v0: "))
num = int(input("Determine N: "))
# Variaveis
i = 0
t = arange(num)
d = zeros(num)

i = 0
# Laço
while (i < size(t)):
	d[i] = a * t[i]**2 / 2. + v0 * t[i]
	i = i +1

#Saida
print (d)