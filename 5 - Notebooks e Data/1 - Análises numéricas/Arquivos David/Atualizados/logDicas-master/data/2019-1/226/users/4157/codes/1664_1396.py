vc =float(input("valor consumido:"))
if(vc <= 300.0):
	vg= vc * 0.1
	print(round(vc+vg, 2))
else:
	vg = vc*0.06
	print(round(vc+vg, 2))