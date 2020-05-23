from numpy import *
media = (array(eval(input("vetor:"))))


while(size(media) > 1):
	nmoni=0
	for i in media:
		if((i>=5) and (i<7)):
			nmoni = nmoni + 1
	print(nmoni)
	media = (array(eval(input("vetor:"))))
	
	
