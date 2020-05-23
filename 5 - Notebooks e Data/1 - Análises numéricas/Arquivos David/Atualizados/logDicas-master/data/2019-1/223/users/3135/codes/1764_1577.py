from numpy import*

a= float(input("Insira a aceleracao do carro:"))
vo = float(input("Insira a velocidade inicial:"))
N= int(input("Insira o valor N:"))
t=arange(N)
d= zeros(N)

d= (a*t**2)/2 + vo*t
print(d)