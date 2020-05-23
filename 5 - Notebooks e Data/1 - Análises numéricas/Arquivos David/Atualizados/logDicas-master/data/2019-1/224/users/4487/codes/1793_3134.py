from numpy import*
v= array(eval(input("digite n numeros: ")), dtype=float)
n=size(v)
i=0
m=0
while(i<size(v)):
	m=m + (v[i])**2
	i= i + 1
M=(1/n)**(1/2)
print(round(M, 2))