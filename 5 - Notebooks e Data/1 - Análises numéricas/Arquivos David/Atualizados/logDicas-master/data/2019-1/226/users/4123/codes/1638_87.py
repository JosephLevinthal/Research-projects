a = int(input())
b = int(input())
c = int(input())
Ca = a<b and a<c
Cb = b<a and b<c
Cc = c<a and c<b
if Ca:
	print(a)
if Cb:
	print(b)
if Cc:
	print(c)