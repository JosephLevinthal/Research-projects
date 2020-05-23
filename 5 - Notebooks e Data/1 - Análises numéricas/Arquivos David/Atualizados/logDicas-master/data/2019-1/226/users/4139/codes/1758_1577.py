from numpy import*

a = float(input("aceleracao: "))
v0 = float(input("velocidade inicial: "))
n = int(input("numero qualquer: "))

i = 0
t = arange(n)
d= zeros(n)

while(i<size(t)):
	d[i] = a*t[i]**2/2 + v0*t[i]
	i = i + 1

print(d)