from numpy import*
v1 = array(eval(input("valor de v1: ")))
v2 = array(eval(input("valor de v2: ")))
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
	elif(v1[c]==pedra and v2[c]papel):
		vb = vb + 1
		
	elif