x= 0
ha = int(input("numero de habitantes a: "))
hb = int(input("numero de habitantes b: "))
pa = float(input("numero de crescimento a: "))
pb = float(input("numero de crescimento b: "))
while(ha < hb):
	ha = ha*(pa/100) + ha
	hb = hb*(pb/100) + hb
	x = x + 1
print(x)
	
	
	