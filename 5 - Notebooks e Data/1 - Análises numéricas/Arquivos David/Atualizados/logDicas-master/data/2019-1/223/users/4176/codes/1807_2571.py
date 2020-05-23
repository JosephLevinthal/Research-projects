s = input("um string: ")
l = ""
for ch in range(len(s)):
	if(s[ch] != "a" and s[ch] != "A"):
		l = l + s[ch]
print(l)