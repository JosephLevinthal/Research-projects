from numpy import*
a=array(eval(input("medias:")))
rp=0
h=0
for i in range(size(a)):
	if(a[i]<5):
		rp+=1
v=zeros(rp, dtype=int)
h=0
for i in range(size(a)):
	if(a[i]<5):
		v[h]=i
		h=h+1
print(rp)
print(v)