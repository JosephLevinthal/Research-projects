s = input("String: ")

inv = ""
i = -1

while (i >= -len(s)):
	inv = inv + s[i]
	i = i - 1
if (s == inv):
	msg = 1
else:
	msg = 0
print(s.replace(" ", "").upper())
print(msg)
