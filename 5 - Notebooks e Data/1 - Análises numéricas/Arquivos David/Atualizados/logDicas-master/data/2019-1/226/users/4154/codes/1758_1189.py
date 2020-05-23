from numpy import *
a = str(input('fala meu bom: '))
print(a.replace(' ', '').upper())
i = 0
j = -1
while i < len(a):
	if a[i] == a[j]:
		i += 1
		j += -1
	else:
		print(0)
		i = len(a)+1
if i == len(a):
	print(1)