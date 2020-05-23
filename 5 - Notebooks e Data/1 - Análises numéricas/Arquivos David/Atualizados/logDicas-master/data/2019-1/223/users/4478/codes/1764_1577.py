from numpy import*
a = float(input("aceleracao do carro: "))
vi = float(input("velocidade incial: "))
n = int(input("numero inteiro: "))

t = arange(n)
d = zeros(n,dtype=int)
v = array(((a*(t**2)/2)) + (vi*t))

print(v)