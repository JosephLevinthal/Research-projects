from numpy import*
a = float(input("aceleracao do carro: "))
vi = float(input("velocidade inicial: "))
n = int(input("numero: "))
vetor = arange(n)
t = vetor[:n]
dt = (a * t **2/2) + vi * t 
print(dt)