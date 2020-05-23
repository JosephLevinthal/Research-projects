from numpy import *
MF = array(eval(input("Medias Finais: ")))

while (size(MF) > 1):
	ap = 0
	
	for x in MF:
		if (x >= 5 and x < 7):
			ap = ap + 1
			
	print(ap)
	
	MF = array(eval(input("Medias Finais: ")))