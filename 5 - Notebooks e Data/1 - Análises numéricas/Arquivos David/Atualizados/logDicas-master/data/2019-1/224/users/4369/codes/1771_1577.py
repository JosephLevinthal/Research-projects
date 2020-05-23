from numpy import*
a = float(input("Digite a bagassa da aceleracao: "))
v = float(input("Digite a v inicial: "))
n = int(input("Digite um n: "))
vt = arange(n)
vd = zeros(n)
vd = ((a * vt ** 2)/ 2) + v * vt
print(vd)