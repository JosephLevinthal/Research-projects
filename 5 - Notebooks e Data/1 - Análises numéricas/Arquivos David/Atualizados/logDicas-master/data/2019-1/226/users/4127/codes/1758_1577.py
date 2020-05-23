from numpy import*
a= float(input("qual a aceleracao do carro?"))
v0= float(input("qual a velocidade inicial do carro? "))
n= int(input("qual o numero inteiro? "))
v1= arange(n)

vd= (a*v1**2/2)+v0*v1
print(vd)
	