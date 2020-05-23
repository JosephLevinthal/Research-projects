from numpy import*
notas=array(eval(input("digite o numero:")))
nomes=array(eval(input("digite o nome:")))
i=0
a=0
b=0
c=0
d=0
f=0
g=0
while(i<size(notas)):
	if(notas[i]==-1):
		a=a+1
	if(notas[i]>=6):
		b=b+1
	if(notas[i]<6 and notas[i]!=-1):
		c=c+1
	if(notas[i]!=-1):
		d=d+ notas[i]
		f=f+1
	if(notas[i]==max(notas)):
		g=nomes[i]
	i=i+1
print(a)
print(b)
print(c)
print(round(d/f,2))
print(g)