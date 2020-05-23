from numpy import*

a = float(input("Aceleracao:"))
vo = float(input("Velocidade inicial:"))
n = int(input("Numero inteiro:"))

t = arange(n)
d = ((a*(t**2))/2) + vo*t
print(d)