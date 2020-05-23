ha  = int(input("Habitantes a: "))
hb  = int(input("Habitantes b: "))
pa = float(input("Percentual de crescimento populacional de a: "))
pb = float(input("Percentual de crescimento populacional de b: "))
pera = pa/100
perb = pb/100
t = 0
ano = 0
while (ha < hb):
	ha = ha + (ha * pera)
	hb = hb + (hb * perb)
	ano = ano + 1
print(ano)
	