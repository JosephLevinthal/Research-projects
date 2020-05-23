
s = input("string de entrada: ")

sv = ""
for i in range(len(s)):
	if(s[i] != "a" and s[i] != "A"):
		sv = sv + s[i]
print(sv)
	