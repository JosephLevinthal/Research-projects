from numpy import*
e = array(eval(input("jogada de Eusapia:")))
b = array(eval(input("jogada de barsanulfo:")))

p = 0 
ve = 0
vb = 0
if(size(e) == size(b)):#quantidade de jogadas
	while(p < size (e) and p < size (b)):
		if (e[p] == b[p]): #empate
			ve = ve
			vb = vb
	
		elif(e[p] == 22 and b[p] == 33 ):
			vb = vb + 1 
		
		elif(e[p] == 33 and b[p] == 22):
			ve = ve + 1
	
		elif(e[p] == 11 and b[p] == 33):
			ve = ve + 1
		
		elif(e[p] == 33 and b[p] == 11):
			vb = vb + 1
		
		elif(e[p] == 11 and b[p] == 22 ):
			vb = vb +1 
		
		elif(e[p] == 22 and b[p] == 11 ):
			ve = ve + 1
			
		p = p + 1	
	
	print(size(e) or size(b))
	if(ve == vb):
		print("EMPATE")
	if (ve > vb):
		print("EUSAPIA")
	if(vb > ve):
		print("BARSANULFO")
		
		
		
	