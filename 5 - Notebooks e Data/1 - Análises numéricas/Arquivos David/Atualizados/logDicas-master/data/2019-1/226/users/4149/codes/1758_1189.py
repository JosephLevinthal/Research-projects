from numpy import*
s=input("escreva a string:")

a=s.replace(" ","")

print(a.upper())
l=len(a)
i=0
k=0
b=-1
m=""
s2=zeros(l,dtype=str)
while(i<len(s)):
	if(s[b]!=" "):
		s2[k]=s[b]
		m=m+s2[k]
		k=k+1
	i=i+1
	b=b-1
if(m==(s.replace(" ",""))):
	r=1
else:
	r=0
print(r)
		
		

