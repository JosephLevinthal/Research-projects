from numpy import*

a = float(input("aceleracao constante:"))
v0 = float(input("velocidade inicial:"))
n = int(input("um numero inteiro:"))
t = 0 
v = arange(n)
d = zeros(n)

while(t < n):
	e = ((a * t**2)/ 2) + v0*t
	d[t] = e
	t = t + 1
print(d)
