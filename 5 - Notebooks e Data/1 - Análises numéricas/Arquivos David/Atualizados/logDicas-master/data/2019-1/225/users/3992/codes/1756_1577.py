from numpy import * 
a = float(input("aceleracao do carro:"))
v = float(input("velocidade inicial do carro:"))
n = array(eval(input("numero:")))
vetor  = arange(n)
t  = vetor[:n]
dt = (a * t ** 2/2 ) + v * t

print(dt)
 