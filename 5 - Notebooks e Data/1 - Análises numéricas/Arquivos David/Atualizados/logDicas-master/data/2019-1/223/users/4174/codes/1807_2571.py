c = input('string:')
b = ""
for ch in range(len(c)):
	if(c[ch] != "a" and c[ch] != "A"):
		b = b + c[ch]
print(b)		
