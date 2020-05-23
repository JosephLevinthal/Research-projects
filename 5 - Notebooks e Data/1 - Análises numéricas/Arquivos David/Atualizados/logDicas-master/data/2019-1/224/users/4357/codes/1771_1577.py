from numpy import*
a=float(input("digite a aceleracao:"))
v=float(input("digite a velocidade:"))
n=int(input("digite o numero:"))
t=arange(n)
d=(a*(t**2))/2+v*t
print(d)