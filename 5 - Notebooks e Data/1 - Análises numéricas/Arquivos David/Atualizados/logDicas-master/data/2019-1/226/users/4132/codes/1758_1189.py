from numpy import *

s = input("Digite: ")

j=0
i=0
cont=0

while(j < len(s) ):
	if(s[j]==" "):
		s=s.replace(" ","")
	j=j+1
s=s.upper()
print(s)

while(i<len(s)):
	k=-1*(i+1)
	if(s[i]==s[k]):
		cont+=1
	i=i+1
if(cont==len(s)):
	print(1)
else:
	print(0)