s = input('Frase: ')
x = ''
for i in range(len(s)):
	if (s[i]=='a' or s[i]=='A'):
		x = x+''
	else:
		x = x+s[i]
print(x)