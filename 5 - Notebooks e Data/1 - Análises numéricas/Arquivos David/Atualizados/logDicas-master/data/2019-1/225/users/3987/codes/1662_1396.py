vc = float(input("valor consumido e:"))
vt1 = vc + (vc * 10/100)
vt2 = vc + (vc * 6/100)
if (vc <= 300):
	print(round(vt1,2))
else:
	print(round(vt2,2))