from numpy import*
a = float(input("aceleracao: "))
vo = float(input("velocidade inicial: "))
n = int(input("n: "))
v = zeros(n)
i = 0
while (i < n):
	d = ((a * (i**2))/2) + vo*i
	v[i] = d
	i = i + 1
print(v)