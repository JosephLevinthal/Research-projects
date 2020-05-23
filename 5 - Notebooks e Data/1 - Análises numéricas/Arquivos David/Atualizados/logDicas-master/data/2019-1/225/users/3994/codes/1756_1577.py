from numpy import*
a = float(input("Digite a acelaracao: "))
v = float(input("Digite a velocidade: "))
N = int(input("Digite n: "))
t = arange(N)
d = zeros(N)

d = (a*(t)**2/2)+v*t
print(d)