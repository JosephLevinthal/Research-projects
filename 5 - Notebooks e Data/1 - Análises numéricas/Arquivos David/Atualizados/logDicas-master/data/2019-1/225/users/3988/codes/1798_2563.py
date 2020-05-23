from numpy import*
v = array(eval(input("medias finais: ")))
while (size(v) > 1):
	ap = 0
	
	for media in v: 
		if (media >= 5) and (media < 7):
			ap = ap + 1
			
	print(ap)
	v = array(eval(input("medias finais: ")))
	

