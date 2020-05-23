from math import*
num=int(input("numero: "))
k=0
n=0
while(k<num):
	n=n+1/factorial(k)
	k=k+1
print(round(n, 8))		  
				  	