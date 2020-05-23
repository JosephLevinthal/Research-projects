from numpy import*

a = float(input("aceleracao: "))
v = float(input("velocidade incial"))
n = int(input(" numero de elementos: "))

t = arange(n)
d = zeros(n)

d = (a * t**2 /2)+v*t

print(array(d))