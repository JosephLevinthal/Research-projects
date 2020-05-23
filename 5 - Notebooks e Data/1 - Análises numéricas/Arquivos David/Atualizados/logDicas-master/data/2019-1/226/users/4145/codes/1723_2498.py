ha = int(input("habitantes na cidade a: "))
hb = int(input("habitantes na cidade b: "))
ca = float(input("crescimento da populacao a: "))
cb = float(input("crescimento da populacao b: "))
t = 0
while(ha<hb):
	crea = ha*(ca/100)
	creb = hb*(cb/100)
	ha = ha + crea
	hb = hb + creb
	t = t+1
print(t)
#print(ha/100)
#print(hb/100)