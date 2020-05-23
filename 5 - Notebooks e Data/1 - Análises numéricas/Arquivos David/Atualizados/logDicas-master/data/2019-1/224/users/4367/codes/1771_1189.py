from numpy import*
a=input("digite a string: ")
i=0
b=""
while(i<len(a)):
	if(a[i]==" "):
		b=b+""
	else:
		b=b+str(a[i])
	i=i+1
print(b.upper())

v=0
ii=0
while(ii<len(b)):
	if(b[ii])==(b[-1*(ii+1)]):
		v=v+1
	ii=ii+1
if(v==len(b)):
	print("1")
else:
	print("0")