from numpy import*

l=array(eval(input('l: ')))
y=array(eval(input('y: ')))

i=0   #contador
f=0   #faltaram
a=0   #aprovados 
pr=0  #reprovados
pm=0  #media
while(size(l)>i):
	if(l[i]==-1):
		f+=1
	if(l[i]>=6)and(l[i]<=10):
		a+=1
	if(l[i]>-1)and(l[i]<6):
		pr+=1
	if(-1<l[i]):
		pm=pm+l[i]
	if(l[i]== max(l)):
		m=y[i]
	i+=1

print(f)
print(a)
print(pr)
print(round(pm/(a+pr),2))
print(m)