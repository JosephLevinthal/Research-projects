ha = int(input("Numero de habitantes cidade A:"))
hb = int(input("Numero de habitantes cidade B:"))
pa = float(input("Porcentagem de crescimento populacional cidade A:"))
pb = float(input("Porcentagem de crescimento populacional cidade B:"))

perca = pa/100
percb = pb/100

ano = 0

while(ha<=hb):
	ha = ha + (ha*perca)
	hb = hb + (hb*percb)
	ano = ano+1
print(ano)	