from numpy import*

a = float(input("Aceleracao: "))
v0 =  float(input("Velocidade inicial: "))
n = int(input("lim: "))

v = arange(n)
t =v[:n] 

d = (a*(t**2))/2 + v0*t

print(d)
	
	
	