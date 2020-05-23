from numpy import*
a=array(eval(input("A aceleracao: ")))
v=array(eval(input("Velocidade inicial: ")))
n=array(eval(input("Numeros inteiros:")))
t=arange(n)
d=zeros(n)
i=0
while(i<n):
	d[i]=((a*(t[i]**2)/2)+v*t[i])
	i=i+1
print(d)
