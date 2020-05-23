ha=int(input("numero de habitantes de a: "))
hb=int(input("numero de habitantes de b: "))
pa=float(input("percentual de crescimento de a(em porcentagem): "))
pb=float(input("percentual de crescimento de b: "))
anos=0
pa = pa / 100
pb = pb / 100
ppa= ha
ppb= hb

while ppa <= ppb:
	ppa = ppa + ppa * pa
	ppb = ppb + ppb * pb
	anos = anos + 1
print(anos)