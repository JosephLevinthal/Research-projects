from numpy import*

x = input("").upper()
a = x.replace(" ","")
print(a)

k=-1
p = ''

while(k >= -len(a)):
	p += a[k]
	k-=1
	
if(p==a):
	print(1)
else:
	print(0)