from numpy import*

a =  float(input("aceleracao: "))
v0 = float(input("velocidade: "))
num = int(input("numero: "))

i=0
t = arange(num)
d = zeros(num)

i = 0

while(i<size(t)):
	d[i]=a*t[i]**2/2+v0*t[i]
	i = i+1
print(d)