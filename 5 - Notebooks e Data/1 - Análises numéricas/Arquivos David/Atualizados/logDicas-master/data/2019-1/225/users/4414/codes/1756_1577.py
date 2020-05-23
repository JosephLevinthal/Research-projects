from numpy import*
a= float(input("acelaracao:"))
v=float(input("velocidade :"))
n= int(input(":"))

vetor = arange(n)
t = vetor[:n]
d = zeros(n)
dt = (a*t**2/2) + v*t
print(dt)