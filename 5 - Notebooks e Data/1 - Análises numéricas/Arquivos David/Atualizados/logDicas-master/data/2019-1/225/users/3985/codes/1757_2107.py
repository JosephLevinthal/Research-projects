from numpy import*

s=input().upper()
a=0
b=0
c=0
while(c<len(s)):
	if(s[c]=="A"or s[c]=="E"or s[c]=="I"or s[c]=="O"or s[c]=="U"):
		a+=1
	else:
		b+=1
	c+=1
print(a)
print(b)