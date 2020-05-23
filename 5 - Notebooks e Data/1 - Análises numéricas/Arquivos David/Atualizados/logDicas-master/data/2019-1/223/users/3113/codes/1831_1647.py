from numpy import*
a=array(eval(input("")))

d=0
s=0
j=0
for i in range(size(a)):
	if(a[i]>=70):
		d=d+1
vet=zeros(d,dtype=int)
for i in range(size(a)):
	if(a[i]>=70):
		s=s+1

print(s)
print(vet)