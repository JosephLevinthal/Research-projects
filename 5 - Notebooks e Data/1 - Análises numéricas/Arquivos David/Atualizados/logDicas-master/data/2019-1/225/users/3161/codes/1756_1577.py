from numpy import*
a = float(input("aceleração do carro: "))
vo = float(input("velocidade inicial:"))
n= int(input("numero inteiro: "))
vetor = arange(n)
t = vetor[:n]
d = zeros(n)
dt = (a*t**2/2) + vo * t
print(dt)