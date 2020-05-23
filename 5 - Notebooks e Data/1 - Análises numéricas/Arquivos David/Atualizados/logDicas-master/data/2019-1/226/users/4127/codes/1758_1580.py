from numpy import*
a= array(eval(input("quais as notas dos alunos? ")))
b= array(eval(input("quais os nomes dos alunos? ")))
t=0
f=0
n=size(a)
while(t<n):
	if(a[t]==-1):
		f=f+1
	t=t+1
print(f)
t=0
ap=0
while (t<n):
	if(a[t]>=6):
		ap=ap+1
	t=t+1
print(ap)
t=0
rp=0
while(t<n):
	if(a[t]<6) and (a[t]!=-1):
		rp=rp+1
	t=t+1
print(rp)
t=0
num=0
den=0
while(t<n):
	if a[t]!=-1:
		num=num+a[t]
		den= den+1
	t=t+1
print(round(num/den, 2))
m=max(a)
t=0
while t<n:
	if m==a[t]:
		m=b[t]
		t=t=1
	else:
		t=t+1
print(m)