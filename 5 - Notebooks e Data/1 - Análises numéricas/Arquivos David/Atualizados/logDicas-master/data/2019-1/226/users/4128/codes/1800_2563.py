from numpy import*

al = array(eval(input("notas:")))

while size(al) > 1:
	nt = 0 
	for x in al:
		if (x >= 5) and (x < 7):
			nt = nt + 1
		
	print(nt)
	
	al = array(eval(input("notas:")))
			