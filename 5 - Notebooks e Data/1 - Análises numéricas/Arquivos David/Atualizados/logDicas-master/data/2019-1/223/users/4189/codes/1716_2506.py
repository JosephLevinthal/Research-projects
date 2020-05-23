peixes = float(input("p:"))
cresc = float(input("p:"))
ret = float(input("p:"))
anos=0
while(0<peixes<12000):
	acresc = peixes * (cresc / 100)
	peixes =peixes + acresc
	peixes = peixes - ret
	anos += 1
if(peixes<=0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(anos)