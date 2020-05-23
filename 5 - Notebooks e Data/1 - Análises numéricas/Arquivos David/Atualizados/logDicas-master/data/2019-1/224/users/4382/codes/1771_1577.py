from numpy import*
a = float(input("digite a aceleracao : "))
V = float(input("digite a velocidade : "))
N = int(input("digite o numero : "))
t = 0
Vt = arange(N,dtype = int)
d0 = (a * Vt**2/2)+V * Vt
print(d0)
