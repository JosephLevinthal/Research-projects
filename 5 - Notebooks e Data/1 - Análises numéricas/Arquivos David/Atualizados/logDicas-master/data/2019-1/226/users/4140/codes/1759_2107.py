from numpy import *
a=input().lower()
i=0
soma1=0
soma2=0
while(i<len(a)):
	if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u"):
		soma1=soma1+1
	else:
		soma2=soma2+1
	i=i+1
print(soma1)
print(soma2)