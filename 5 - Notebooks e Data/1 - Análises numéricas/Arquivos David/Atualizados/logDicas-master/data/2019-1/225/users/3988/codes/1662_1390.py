n = float(input("tempo:"))
if (n >= 100):
	x = (25 + (1.40 * n))
else:
	x = (1.20 * n)
print(round(x, 2))	