from math import*

a=eval(input("entre com o angulo:"))
k=int(input("entre com a constante:"))

i=0
j=1
b=0
while(k>i):
	b=((j**(i+1)/factorial(i))*(-1*i))+b
	
	i=i+1
	j=j+1
print(a)	
	