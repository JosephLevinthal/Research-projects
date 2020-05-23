from numpy import*

a = float(input("Insira a aceleracao do carro: "))
v0 = float(input("Insira v0: "))
N = int(input("Insira o N: "))
d = zeros(N)
t = arange(N)
i = 0

while(i < N):
	d[i] = (a * t[i]**2 / 2) + v0 * t[i]
	i = i + 1

print(d)