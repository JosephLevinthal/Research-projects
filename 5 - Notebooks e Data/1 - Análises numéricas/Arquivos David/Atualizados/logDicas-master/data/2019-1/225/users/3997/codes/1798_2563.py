from numpy import*

medias = array(eval(input()))

while (size(medias)>1):
	ap = 0
	for i in medias:
		if (i>=5 and i<7):
			ap+=1
	print(ap)
	medias = array(eval(input()))