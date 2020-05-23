from numpy import *
a = float(input("aceleracao: "))
vo = float(input("velocidade inicial: "))
n = int(input("n: "))
t = arange(n, dtype=int)
d = zeros(n, dtype=int)
d = ((a*t**2)/2) + vo*t
print(d)