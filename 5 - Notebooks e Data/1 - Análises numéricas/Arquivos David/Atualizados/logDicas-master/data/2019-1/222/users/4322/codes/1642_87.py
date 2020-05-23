a=int(input())
b=int(input())
c=int(input())

if (a<b<c) or (a<c<b):
	print(a)
if (b<a<c) or (b<c<a):
	print(b)
if (c<a<b) or (c<b<a):
	print(c)
	