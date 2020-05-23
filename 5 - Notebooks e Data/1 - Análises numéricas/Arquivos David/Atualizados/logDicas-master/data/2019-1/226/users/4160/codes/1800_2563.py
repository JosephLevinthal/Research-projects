from numpy import *

v = array(eval(input("Medias finais: ")))

while(size(v)>1):
	nmonitor = 0
	
	for i in v:
		if(i>=5 and i<7):
			nmonitor = nmonitor + 1
	print(nmonitor)
	
		
	v = array(eval(input("Medias finais: ")))
	

	