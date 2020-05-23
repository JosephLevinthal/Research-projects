vc= float(input("Qual o valor consumido?"))
g= vc * 0.1

if (vc <= 300):
	vt = vc + g
else:
	vt = vc
print(round(vt, 2)