from numpy import*

v= array(eval(input("Poe as notas finais ai:")))

while(size(v)>1):
	c=0	
	for i in v:
		if(i>=5 and i<7):
			c+=1
	print(c)
	v = array(eval(input("Proximo vetor: "))),0