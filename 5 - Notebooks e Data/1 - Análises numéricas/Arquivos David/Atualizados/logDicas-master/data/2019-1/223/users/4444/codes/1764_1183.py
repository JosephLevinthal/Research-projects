from numpy import *
a=array(eval(input('digite o vetor de notas:  ')))
b=array([])
qtd_pos=0
i=0
while(i<size(a)):
	if(a[i]>0):
		qtd_pos=qtd_pos+1
		i=i+1
	else:
		i+=1
b = arange(qtd_pos)
x=0
y=0
while(x<len(a)):
	if(a[x]>0):
		b[y]=a[x]
		y=y+1
		x=x+1
	else:
		x=x+1
print(b)
