from numpy import*
a=eval(input("digite as letras: "))
v=zeros(size(a), dtype=str)
c=0
for i in range (size(a)-1,-1,-1):
	v[c]=v[c]+""+a[i]
	c=c+1
print(v)