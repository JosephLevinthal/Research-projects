from numpy import*
a= int(input("numero de asteriscos: "))
k=a
for i in range(a):
	print("*"*a)
	a= a-1
a = a +1
for i in range(k):
	print("*"*a)
	a=a+1

