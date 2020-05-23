from numpy import *
a = array(eval(input("Aceleracao: ")))
v = array(eval(input("Velocidade: ")))
N = int(array(eval(input("Numero: "))))
t = arange(N)
d = zeros(N)

d = ((a * t**2) / 2) + v * t

print(d)