ha=float(input("No de habitantes da cidade A: "))
hb=float(input("No de habitantes da cidade B: "))
pa=float(input("Percentual de crescimento de A: "))
pb=float(input("Percentual de crescimento de B: "))
anos=0
ha1=ha
hb1=hb
while(ha1<hb1):
	ha1=ha1 + ha1 * (pa/100)
	hb1=hb1 + hb1 * (pb/100)
	anos=anos+1

print(anos)