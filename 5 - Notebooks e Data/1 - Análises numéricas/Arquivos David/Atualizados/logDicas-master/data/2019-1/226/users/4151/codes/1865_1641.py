from numpy import*
v=array(eval(input("digite: ")))
t=0
for i in range(size(v)):
	if(v[i]%3==0):
		t=t+1
print(t)

a=0
v2=zeros(t, dtype=int)
for j in range(size(v)):
	if(v[j]%3==0):
		v2[a]=j
		a=a+1
		
print(v2)
