from numpy import*

s=input().lower()
c=0
while(c<len(s)):
	if(s[c]=="a"or s[c]=="e"or s[c]=="i"or s[c]=="o"or s[c]=="u"):
		s = s.replace(s[c],"")
	c+=1
print(s)