from numpy import*
n=int(input("quantidade:"))

k=zeros((n,n),dtype=int)
g=zeros((n,n),dtype=int)
h=1
for i in range(n):
	for j in range(n):
		if(i==j):
			k[i,:]=h
			k[:,j]=h
			h=h+1
		g[i,j]=k[i,j]	

print(g)