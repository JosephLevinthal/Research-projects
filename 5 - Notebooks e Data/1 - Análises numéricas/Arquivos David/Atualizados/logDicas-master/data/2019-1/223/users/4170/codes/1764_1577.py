from numpy import*
a = float(input("Aceleracao: "))
v0 = float(input("Velocidade inicial: "))
N = int(input("Numero inteiro: "))
t = arange(N)
d = zeros(N, dtype=int)
v = (a*(t**2)/2+v0*t-d)
print(v)