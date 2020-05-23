x = input()

h = 0
v = ""
while len(x) > h:
	if len(x) % 3 == 0 and len(x) >= 3:
		y = x[h:h+3]
		
		if h < len(x) - 3:
			v += y + "."
		else:
			v += y
			
	h += 3
	
print(v)