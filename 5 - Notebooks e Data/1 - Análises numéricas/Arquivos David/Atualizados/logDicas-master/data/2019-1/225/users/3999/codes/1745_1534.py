x=float(input())
k=int(input())
tgh= x+(x**(2*k+1))/2*k+1
i=0
while(-1<x<1 and k>0):
	i=x+(x**(2*k+1))/k+2*k+1+tgh
	print(round(i,7))