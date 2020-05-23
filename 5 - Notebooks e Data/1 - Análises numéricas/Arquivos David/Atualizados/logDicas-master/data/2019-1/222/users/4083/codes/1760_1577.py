from numpy import*

ac = float(input("digite a aceleracao do carro: "))
v0 = float(input("digite a velocidade inicial do carro: "))
n = int(input("digite a valor n: "))
t = 0
d = arange(n)
d = zeros(n)

t = arange(n)

i = 0

while (i != n):
		d =(ac*(t**2)/2) + v0
		
		i = i + 1
		
print(d)

