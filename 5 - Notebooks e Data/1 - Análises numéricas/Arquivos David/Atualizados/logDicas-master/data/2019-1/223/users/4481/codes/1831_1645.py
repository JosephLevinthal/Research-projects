from numpy import*
a = array(eval(input('quantos saques foram efuados: ')))
b=0
for i in range(size(a)):
	if(a[i] >= 2000):
		b=b+1
c=zeros(b, dtype=int)
d=0
for i in range(size(a)):
	if(a[i]>=2000):
		c[d]=i
		d=d+1
print(b)
print(d)