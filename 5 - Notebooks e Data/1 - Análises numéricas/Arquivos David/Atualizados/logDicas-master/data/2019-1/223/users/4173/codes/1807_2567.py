from numpy import*
a = int(input())
f = "*"
for i in range(a):
	b = f*(a-i) 
	print(b)
for i in range(a):
	b = f*(i+1)
	print(b)
	