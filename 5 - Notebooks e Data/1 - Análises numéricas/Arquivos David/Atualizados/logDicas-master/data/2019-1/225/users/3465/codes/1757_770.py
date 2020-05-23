from numpy import *
a =  input("")
b =  input("")
a = a.lower()
b = b.lower()
v1 = array([0]*26)
for i in range(len(a)):
	v1[ord(a[i])-ord('a')]+=1
	v1[ord(b[i])-ord('a')]-=1
print(v1)
if(v1.sum()!=0):
	print(0)
else:
	print(1)
