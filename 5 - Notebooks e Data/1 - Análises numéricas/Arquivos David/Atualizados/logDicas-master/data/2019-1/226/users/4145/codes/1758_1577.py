from numpy import*
a = float(input("aceleracao: "))
v0 = float(input("velocidade inicial: "))
n = int(input("numero de repeticoes: " ))
t=arange(n)
d =zeros(n,dtype=int)
d = (a*t**2)/2 + v0*t
print(d)
	