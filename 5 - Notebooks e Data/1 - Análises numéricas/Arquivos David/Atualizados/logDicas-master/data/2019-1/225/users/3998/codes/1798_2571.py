s= input(": ")
j= ''
for i in range(len(s)):
	if(s[i].upper()!= "A"):
		j= j + s[i]
	elif(s[i].upper()== "A"):
		j=j
print(j)