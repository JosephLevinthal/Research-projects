s = input("Digite a string: ")
x = ""
for i in range(len(s)):
	if(s[i] == "a" or s[i] == "A"):
		i = i
	else:
		x = x + s[i]
print(x)
	
	