n=int(input("entradas: "))
f=1
l=2
t=3
p=4
e=1
i=0
soma=3
while(f<=n):
	soma=soma +i
	i=((-4)/(l*t*p))*(-1)**e
	f=f+1
	l=l+2
	t=t+2
	p=p+2
	e=e+1
print(round(soma,8))