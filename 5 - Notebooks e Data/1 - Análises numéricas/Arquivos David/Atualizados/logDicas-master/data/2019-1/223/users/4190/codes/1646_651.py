a = float(input('Altura: '))
s = input('Sexo: ')

if s=='M' or s=='m':
	r = ((62.1*a)-44.7)
	print(round(r, 2))
else:
	r = ((72.7*a)-58)
	print(round(r, 2))