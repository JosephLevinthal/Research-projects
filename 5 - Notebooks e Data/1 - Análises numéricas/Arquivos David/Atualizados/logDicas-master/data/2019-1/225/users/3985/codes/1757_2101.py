from numpy import*

n= int(input())
w= zeros(n, dtype=int)
w[0]=0
w[1]=1
z=2
while(z<n):
	w[z]=w[z-1]+w[z-2]
	z+=1
print(w)