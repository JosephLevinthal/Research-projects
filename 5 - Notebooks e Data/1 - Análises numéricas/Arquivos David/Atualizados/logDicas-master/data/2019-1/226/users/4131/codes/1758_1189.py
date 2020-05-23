from numpy import*
v =input("letra:")
b = v.replace(" ","").upper()
a = 0
t=0
print(b)
while(t<len(v)):
	if(v[t]==v[-1*(t+1)]):
		a+=1
	t+=1
if(a==len(v)):
	print(1)
else:
	print(0)