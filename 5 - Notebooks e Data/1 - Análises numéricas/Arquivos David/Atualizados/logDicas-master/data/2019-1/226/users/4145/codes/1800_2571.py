s=input("string desejada: ")
ss=""
for i in range(len(s)):
	if(s[i]=="a" or s[i]=="A"):
		i=i
	else:
		ss=ss+s[i]
print(ss)		
		