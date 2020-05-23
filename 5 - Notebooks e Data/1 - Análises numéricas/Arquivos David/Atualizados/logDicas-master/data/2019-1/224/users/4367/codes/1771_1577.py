from numpy import*
a=float(input("diga a aceleracao: "))
vi=float(input("diga a velocidade inicial: "))
n=int(input("diga um numero inteiro positivo: "))
t=arange(n)
d=zeros(n)
d=((a*(t**2))/2)+(vi*t)
print(d)