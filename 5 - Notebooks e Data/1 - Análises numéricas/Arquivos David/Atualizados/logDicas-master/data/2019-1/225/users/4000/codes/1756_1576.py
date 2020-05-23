from numpy import*
v1 = array(eval(input("Valor de v1: ")))
v2 = array(eval(input("Valor de v2: ")))
pedra = 11
papel = 22
tesoura = 33
c = 0
ve = 0
vb = 0
eu = "EUSAPIA"
ba = "BARSANULFO"
e = "EMPATE"
while(c<size(v1)):
	if(v1[c]==pedra and v2[c]== tesoura):
		ve = ve + 1
	elif(v1[c]==pedra and v2[c]==papel):
		vb = vb +1
		
	elif(v1[c]==tesoura and v2[c]== pedra):
		vb = vb +1
	elif(v1[c]==tesoura and v2[c]== papel):
		ve = ve +1
	elif(v1[c]==papel and v2[c]== pedra):
		ve = ve +1
	elif(v1[c]==papel and v2[c]==tesoura):
		vb = vb +1
	c = c+1
print(size(v1))
if(ve>vb):
	print(eu)
elif(vb>ve):
	print(ba)
else:
	print(e)
	

	
		
		
	
		
	
