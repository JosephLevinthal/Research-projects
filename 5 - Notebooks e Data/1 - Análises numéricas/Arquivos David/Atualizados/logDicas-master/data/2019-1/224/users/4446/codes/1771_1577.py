from numpy import *
a= float(input("digite a aceleracao: "))
v0= float(input("digite a velocidade inicial: "))
n= int(input("digite um numero: "))
t= arange(n , dtype=int)

d= (a* t**2)/ 2 + v0 * t

print(d)