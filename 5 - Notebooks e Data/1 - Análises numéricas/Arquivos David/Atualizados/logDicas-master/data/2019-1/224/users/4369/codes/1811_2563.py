from numpy import*
v = array(eval(input("Digite as medias: ")))
ap = 0
while size(v) > 1:
	for i in v:
		if i >= 5 and i < 7:
			ap += 1
	print(ap)
	ap = 0 
	v = array(eval(input("Digite as medias: ")))	