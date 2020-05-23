from numpy import*

a = float(input("Aceleracao: "))
v = float(input("Velocidade inicial: "))
n = int(input("numero: "))

t = arange(n)

x = (((t**2)*a)/2)+v*t


print(x)