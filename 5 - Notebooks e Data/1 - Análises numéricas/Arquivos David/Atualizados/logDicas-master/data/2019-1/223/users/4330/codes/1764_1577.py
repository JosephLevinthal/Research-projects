from numpy import*
a = float(input("aceleracao do carro:"))
v0 = float(input("velocidade do carro:"))
N = int(input("um numero inteiro positivo:"))

t = arange(N)
d = zeros(N)
posi = 0
while(posi < N):
	d[posi] = a * (t[posi]**2)
	v0t = v0 * t[posi]
	d[posi] = (d[posi]/2) + v0t
	posi = posi + 1
print(d)