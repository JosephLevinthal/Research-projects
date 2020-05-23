from numpy import*

a=float(input("Aceleracao:"))
vo=float(input("Velocidade inicial:"))
n= int(input("quant:"))
t= arange(n)
d=zeros(n)

d=(a*(t**2)/2)+vo*t
print(d)