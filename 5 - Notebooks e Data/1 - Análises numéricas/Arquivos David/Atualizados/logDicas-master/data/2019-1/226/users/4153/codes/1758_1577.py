from numpy import *

# Aceleracao constante a
a = float(input("Insira a aceleracao: "))
# Velocidade inicial v0
v0 = float(input("Insira a velocidade inicial: "))
# numero inteiro N
n = int(input("Insira um numero inteiro n: "))

# equacao:
v = zeros(n)
i = 0
while(i < n):
	d = ((a * (i ** 2))/(2)) + (v0 * i)
	v[i] = d
	i = i + 1
print(v)