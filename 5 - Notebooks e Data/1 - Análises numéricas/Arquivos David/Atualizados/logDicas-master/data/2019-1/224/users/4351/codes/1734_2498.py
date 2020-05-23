ha= int(input("numeros de habitantes da cidade a: "))
hb= int(input("numeros de habitantes da cidade b: "))
pa= float(input("percetual de crescimento a: "))
pb= float(input("percetual de crescimento b: "))
tca = pa/100
tcb = pb/100
anos= 0
ppa = ha
ppb = hb

while (ppb>ppa):
	ca = ppa*tca
	cb = ppb*tcb
	ppa= ppa+ca
	ppb= ppb+cb
	anos= anos+1
print(anos)