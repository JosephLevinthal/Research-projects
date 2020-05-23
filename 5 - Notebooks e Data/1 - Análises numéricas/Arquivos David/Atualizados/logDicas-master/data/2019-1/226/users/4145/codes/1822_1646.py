from numpy import*
s= array(eval(input("saques efetuados: ")))
m=0
w=0
for i in range(size(s)):
	if(s[i]<=50):
		m=m+1
x= zeros(m,dtype=int)
for i in range(size(s)):
	if(s[i]<=50):
		x[w]=i
		w=w+1
print(m)
print(x)