a=int(input("numero1:"))
b=int(input("numero2:"))
c=int(input("numero3:"))
if(a<c and a>b):
	M = a
if(a>c and a<b):
	M = a
if(b<c and b>a):
	M = b
if(b>c and b<a):
	M = b
if(c<b and c>a):
	M = c
if(c>b and c<a):
	M = c
print(M)