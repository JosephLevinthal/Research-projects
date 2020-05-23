from numpy import *

b=float(input("digite: ")) #aceleracao
vo=float(input('digite: ')) # velocidade inciaal
inteiro=int(input('digite: ')) 
t=arange(inteiro)
d=zeros(inteiro)
i=0
while(i<inteiro):
	d[i]=(b*t[i]**2)/2 + vo*t[i]
	i=i+1
print(d)
	

