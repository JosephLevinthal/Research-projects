a = str(input('fala meu bom: '))
b = ''
i = 0
j = 0
while i < len(a):
	if len(a)>3:
		b += a[i:i+3] + '.'
	else:
		print(a)
	i +=3
print(b[0:-1])