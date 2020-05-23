from numpy import*
a= float(input("aceleracao:"))
v0=float(input(":"))
n= int(input("numero:"))

v=arange(n)
t=v[:n]
d= (a*(t**2))/2 + v0*t

print(d)