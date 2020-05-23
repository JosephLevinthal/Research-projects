from numpy import*
g= array(eval(input("insira o numero de gols efetuados por esse time em cada partida: ")))
gt=array(eval(input("insira o numero de gols efetuados pelo time adversario: ")))
a= zeros(3, dtype=int)
v=0
e=0
d=0
for i in range(size(g)):
	if g[i]>gt[i]:
		a[0]=a[0]+1
	elif g[i]==gt[i]:
		a[1]=a[1]+1
	elif g[i]<gt[i]:
		a[2]=a[2]+1
print(a)
		
