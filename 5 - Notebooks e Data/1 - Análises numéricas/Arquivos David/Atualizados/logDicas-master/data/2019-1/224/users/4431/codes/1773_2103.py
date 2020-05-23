from numpy import*
y=array(eval(input("Digtie um vetor: ")))
x=array(eval(input("Digite um vetor: ")))
i=0
u=-1
h=1
m=zeros(len(x),dtype=int)
if(len(x)%2==0):
	while(len(x)>h):
		m[i]=x[u]
		m[u]=x[i]
		h=h+1
		i=i+1
		u=u-1
else:
	h=0
	l=len(x)
	b=len(x)//2
	while(b>h):
		m[i]=x[u]
		m[u]=x[i]
		m[b]=x[b]
		h=h+1
		i=i+1
		u=u-1
t=0		
while((len(x))>t):
	if(m[t]>y[t]):
		print(m[t])
		t=t+1
	else:
		print(y[t])
		t=t+1
		