from numpy import*
m=array(eval(input("insira as matriculas dos alunos: ")))
s=0
sm=0
for i in m:
	if i%2==0:
			s=s+1
	else:
		sm=sm+1
z=zeros(sm,dtype=int)
x=0
for i in range(size(m)):
	if m[i]%2!=0:
		z[x]=m[i]
		x=x+1
print(z)	
