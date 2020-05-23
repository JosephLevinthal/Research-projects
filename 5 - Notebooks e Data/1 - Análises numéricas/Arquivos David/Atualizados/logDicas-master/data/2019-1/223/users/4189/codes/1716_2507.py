peixes = float(input("p:"))
cresc = float(input("p:"))
anos=0
while(0<peixes<8000):
	ret = float(input("p:"))
	acresc = peixes * (cresc / 100)
	peixes =peixes + acresc
	peixes = peixes - ret
	anos += 1
if(peixes<=0):
	print("ZERO")
else:
	print("MAXIMO")
print(anos)