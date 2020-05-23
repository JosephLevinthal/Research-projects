from numpy import *
n=array(eval(input("notas: ")))
a=array(eval(input("alunos: ")))
i=0
f=0
ap=0
re=0
s=0
p=0
no = 0
siz = 0
while(i<size(n)):
	if(n[i]==-1):
		f=f+1
	if(n[i]>=6):
		ap=ap+1
	if(n[i]<6 and n[i]!=-1):
		re=re+1
	if(max(n)==n[i]):
		no = a[i] 
	if(n[i] != -1):
		s = s + n[i]
		siz = siz + 1
	i = i + 1
m=s/siz
print(f)
print(ap)
print(re)
print(round(m, 2))
print(no)