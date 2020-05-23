s = input("String: ").lower()
v = 0
c = 0
for i in range(len(s)):
	if(s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u"):
		v = v + 1
	else:
		c = c + 1
print(v)
print(c)
	