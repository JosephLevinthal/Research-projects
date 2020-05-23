p = int(input("Posicao: "))
g = 0

while (p != 0):
	p = int(input("Posicao: "))
	if (p == 1):
		g1 = 20
	elif (p == 2):
		g1 = 15
	elif (p == 3):
		g1 = 10
	elif (4 <= p <= 10):
		g1 = 11 - p
	elif (p < 0):
		g1 = 0
	else:
		g1 = 0	
	g = g + g1

if (p == 1):
	g2 = 20
elif (p == 2):
	g2 = 15
elif (p == 3):
	g2 = 10
elif (4 <= p <= 10):
	g2 = 11 - p
elif (p < 0):
	g2 = 0
else:
	g2 = 0

total = g + g2

print(total)
