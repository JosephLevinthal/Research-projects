p1 = float(input("peso da encomenda:"))

if (p1 <= 4999.9):
	vf = 0.05 * p1
else:
	vf = (0.04 * p1) + 60
print(round(vf , 2))
