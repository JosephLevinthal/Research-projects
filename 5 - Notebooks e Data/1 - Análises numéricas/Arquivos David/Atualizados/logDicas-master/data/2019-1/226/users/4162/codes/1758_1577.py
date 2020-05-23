from numpy import*
a=float(input("insira a aceleracao do carro: "))
v=float(input("insira a velocidade inicial do carro: "))
t= int(input("insira os instantes: "))
n=arange(t)
d=(a*(n**2))/2+v*n
print(d)