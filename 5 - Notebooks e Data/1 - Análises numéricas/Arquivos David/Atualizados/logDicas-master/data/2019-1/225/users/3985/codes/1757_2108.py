from numpy import*

s=input().lower()
c=0
while(c<len(s)):
	if(s[c]!="a"and s[c]!="e"and s[c]!="i"and s[c]!="o"and s[c]!="u"):
		s = s.replace(s[c],"p")
	c+=1
print(s)