from numpy import*
a = float(input("Insira a aceleracao: "))
v0 = float(input("Insira a velocidade inicial: "))
N = int(input("Insira um numero: "))
d = zeros(N)
t = arange(N)
i = 0

while(i < N):
	d[i] = (a * t[i]**2 / 2) + v0 * t[i]
	i = i + 1
print(d)




