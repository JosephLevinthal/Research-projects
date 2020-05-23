from numpy import*
a = float(input("Aceleracao do carro: "))
vo = float(input("Velocidade inicial: "))
n = int(input("numero inteiro: "))
vetor = arange(n)
t = vetor[:n]
d = zeros(n)
dt = (a*t**2/2) + vo * t
print(dt)
