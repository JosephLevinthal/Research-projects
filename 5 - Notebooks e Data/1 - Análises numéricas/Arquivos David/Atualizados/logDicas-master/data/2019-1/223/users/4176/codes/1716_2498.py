ha = int(input('Habitantes da cidade A: '))
hb = int(input('Habitantes da cidade B: '))
ca = float(input('Crescimento de A: '))
cb = float(input('Crescimento de B: '))

anos = 0

while (ha < hb):
	ha= ha + (ca*ha)/100
	hb= hb + (cb*hb)/100
	anos = anos + 1
print(anos)
	
