x = input()

s = ""

for i in range(len(x)):
	if(x[i].upper() != "A"):
		s = s + x[i]

print(s)		