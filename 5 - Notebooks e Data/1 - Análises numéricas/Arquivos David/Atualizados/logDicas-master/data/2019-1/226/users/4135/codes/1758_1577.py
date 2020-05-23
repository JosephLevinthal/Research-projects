from numpy import*
a = float(input("Digite o valor da aceleraçao:"))
vo = float(input("Digite o vaalor da velocidade:"))
n = int(input("Digite um numero positivo:"))

t = arange(n)
d = (zeros(n, dtype = int))

d = ((a*(t**2))/2)+vo*t

print(d)

	
