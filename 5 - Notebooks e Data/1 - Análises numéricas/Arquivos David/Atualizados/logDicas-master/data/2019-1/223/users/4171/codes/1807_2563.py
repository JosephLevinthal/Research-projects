from numpy import *

mediaf = array(eval(input("medias finais: ")))

while size(mediaf) > 1:
		
	naomonitores = 0
		
	for x in mediaf:
		
		if x >= 5 and x < 7:
		naomonitores += 1
	
	print(naomonitores)
	
	mediaf = array(eval(input("dnv: ")))