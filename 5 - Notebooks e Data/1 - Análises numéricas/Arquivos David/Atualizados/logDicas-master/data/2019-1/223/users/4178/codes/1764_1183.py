from numpy import *

bb = array(eval(input("Entrada: ")))

for bb in bb:
	if bb <=0:
		bb.remove(bb)
		
	
print(bb)
