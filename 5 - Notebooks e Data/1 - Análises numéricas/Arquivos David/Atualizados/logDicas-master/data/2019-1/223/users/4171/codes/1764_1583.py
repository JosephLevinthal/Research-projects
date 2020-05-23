s = input("")

i = 0
v = ""

while i < len(s):
	if len(s) % 3 == 0 and len(s) >= 3:
		
		x = s[i:i+3]
		
		if i < len(s) - 3:
			v += x + "."
		else:
			v += x
		
		i += 3
		

print(v)