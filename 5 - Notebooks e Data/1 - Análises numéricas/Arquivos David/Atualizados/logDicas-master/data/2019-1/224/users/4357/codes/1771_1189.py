from numpy import*
strings= input("digite o string:")
copy=""
i=0
while(i<len(strings)):
	if(strings[i]==" "):
		copy=copy+""
	else:
		copy=copy+str(strings[i])
	i=i+1
print(copy.upper())
v=0
a=0
while(a<len(copy)):
	if(copy[a]==copy[-1*(a+1)]):
		v=v+1
	else:
		v=v+0
	a=a+1
if(v==len(copy)):
	print("1")
else:
	print("0")