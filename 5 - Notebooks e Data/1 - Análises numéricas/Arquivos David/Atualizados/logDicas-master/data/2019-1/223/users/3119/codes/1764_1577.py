from numpy import*

a = float(input("Aceleracao: "))
v = float(input("Velocidade inicial: "))
n = int(input("N: "))

t = arange(n)
d = zeros(n)

d = (a * t ** 2/ 2 ) + v * t


print(d)