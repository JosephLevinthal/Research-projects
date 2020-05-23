from numpy import*
x=float(input("Digite a aceleracao: "))
y=float(input("Digite a velocidade incial do carro: "))
z=int(input("Digite um numero postivo: "))
q=arange(z)
g=zeros(z)
d=0
f=0
h=0
while(h<(z)):
	t=((x*(q[f]**2))/2)+y*f
	g[f]=(g[f]+t)
	h=h+1
	f=f+1
print(g)	
	