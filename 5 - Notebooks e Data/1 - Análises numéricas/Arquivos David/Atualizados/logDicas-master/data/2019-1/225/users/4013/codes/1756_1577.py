from numpy import*
a = float(input("aceleracao:"))
vo = float(input("velocidade inicial:"))
n = int(input("numero:"))
t = arange(n)
d = zeros(n)
d = (a * (t ** 2))/2 + (vo * t)
print(d)