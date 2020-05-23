from numpy import*
a = float(input("Aceleracao: "))
v0 = float(input("Velocidade: "))
n = int(input("Numero inteiro: "))

i = 0
fim = n-1
t = arange(n) 
d = zeros(n,dtype=float)
d = (a * (t**2))/2 + v0 * t

print(d)

