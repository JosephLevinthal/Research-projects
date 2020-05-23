s=input("qualquer:").upper()

c=0
v=0

for i in range(len(s)):
	if(s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U"):
		v=v+1
	else:
		c+=1
		
print(v)
print(c)