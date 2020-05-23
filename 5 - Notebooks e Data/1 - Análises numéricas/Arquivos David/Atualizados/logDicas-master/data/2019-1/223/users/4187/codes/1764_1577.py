from numpy import*
a = float(input("aceleracao do carro:"))
v0 = float(input("velocidade do carro:"))
N = int(input("um numero inteiro positivo:"))

t = arange(N)
d = zeros(N)
i = 0
while(i < N):
	d[i] = a * (t[i]**2)
	v0t = v0 * t[i]
	d[i] = (d[i]/2) + v0t
	i = i + 1
print(d)