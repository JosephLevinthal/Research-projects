from numpy import *
ac= float(input("aceleracao:"))
vi= float(input("velocidade inicial:"))
num= int(input("numero:"))
i=0
t=arange(num)
d= zeros(num)

while(i<size(t)):
	d[i]= ((ac*t[i]**2) /2) + vi*t[i]
	
	i=i+1
print(d)


