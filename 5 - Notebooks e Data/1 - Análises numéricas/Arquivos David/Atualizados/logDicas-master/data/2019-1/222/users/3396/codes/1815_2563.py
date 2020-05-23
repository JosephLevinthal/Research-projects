from numpy import*
v = array(eval(input("Medias finais:  ")))

while (size(v) > 1):
	ap = 0
	for i in v:
		if (i >= 5 and i< 7):
			ap = ap + 1
	
	print(ap)
	v = array(eval(input("Medias finais:  ")))