from numpy import*

a = float(input("aceleracao: "))
v0 = float(input("velocidade inicial: "))
n = int(input("numero N positivo: "))

t = arange(n)  #vetor tempo
d = zeros(n)    #vetor distancia
x = 0           #variavel tempo

while x < size(t):
	d[x] = ((a * (t[x] ** 2))/2) + (v0 * t[x])
	x = x + 1
print(d)