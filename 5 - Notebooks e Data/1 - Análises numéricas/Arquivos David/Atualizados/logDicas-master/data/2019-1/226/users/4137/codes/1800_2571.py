s = input()
x = ""

for i in range(len(s)):
	if s[i].lower() != "a" :
		x = x + s[i]
print(x)