tempo = float(input("tempo de voo: "))
p1 = 5000
min1 = 100
p2 = 8000
min2 = 90
eq1 = (p1 + (tempo*min1))
eq2 = (p2 + (200*min1) + ((tempo - 200)*min2))
if tempo <= 200:
	print(round(eq1, 2))
else:
	print(round(eq2, 2))