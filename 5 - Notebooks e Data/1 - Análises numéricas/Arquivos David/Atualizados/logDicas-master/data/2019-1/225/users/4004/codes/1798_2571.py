n = str(input("string: "))

s = ""

for i in n:
	if i.upper() != "A":
		s = s + i
	else:
		s = s
print(s)