from numpy import*
a = float(input("digite a aceleracao: "))
vo = float(input("digite v0: "))
n = int(input("digite o numero inteiro: "))
v1 = arange(n)
vd = (a*v1**2)/2 + vo*v1
print(vd)