from numpy import*
x=int(input("Digite um numero inteiro: "))
q=0
w=1
r=zeros(x,dtype=int)
r[1]=1
t=2
while(x>t):
	r[t]=r[q]+r[w]
	t=t+1
	w=w+1
	q=q+1
	
print(r)