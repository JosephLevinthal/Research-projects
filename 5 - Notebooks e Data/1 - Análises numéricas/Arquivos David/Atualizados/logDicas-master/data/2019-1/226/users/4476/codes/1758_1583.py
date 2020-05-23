n = input("digite: ")

i = 0
k = 3
m = ""

while (i<len(n)):
	if (i==(len(n)-3)):
		m = m + n[i:k]
		i = i + 3
		k = k + 3
	else:
		m = m + n[i:k] + "."
		i = i + 3
		k = k + 3
print(m)
