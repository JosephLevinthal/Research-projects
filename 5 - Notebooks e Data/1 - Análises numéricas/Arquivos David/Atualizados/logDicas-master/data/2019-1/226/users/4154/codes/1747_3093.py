a = 'a'
b = 0
c = 0
while a.lower() != 'x':
	a = str (input('valor do jogo'))
	if a.lower() == 'v':
		b += 3
	elif a.lower() == 'e':
		c += 1
print(b)
print(c)