from numpy import*
a = array(eval(input('jogadas eusapia')))
b = array(eval(input('jogadas do outro')))
ab = 0
ba = 0
print(size(a))
i = 0
while i < size(a):
	if (a[i]==11) and (b[i]==22):
		ba += 1
	elif (b[i]==11) and (a[i]==22):
		ab += 1
	elif (a[i]==22) and (b[i]==33):
		ba += 1
	elif (b[i]==22) and (a[i]==33):
		ab += 1
	elif (a[i]==33) and (b[i]==11):
		ba += 1
	elif (b[i]==33) and (a[i]==11):
		ab += 1
	i += 1
if ab>ba:
	print('EUSAPIA')
elif ba>ab:
	print('BARSANULFO')
elif ab == ba:
	print('EMPATE')