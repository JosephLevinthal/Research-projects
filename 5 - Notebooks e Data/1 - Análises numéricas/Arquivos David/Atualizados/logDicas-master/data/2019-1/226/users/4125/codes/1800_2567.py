from numpy import*
x = int(input("numero de asteriscos: "))
k = x
for i in range(x):
	print("*"*x)
	x = x - 1
x = x + 1
for j in range(k):
	print("*"*x)
	x = x + 1