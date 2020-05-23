from numpy import*
Eu= array(eval(input("numero da jogada:")))
Bar= array(eval(input("numero de jogada:")))
i=0
vu=0
vr=0
pedra=11
papel=22
tesoura=33

while(i< size(Eu)):
	if(Eu[i]==pedra and Bar[i]==tesoura):
		vu=vu+1
		
	elif(Eu[i]==papel and Bar[i]==pedra):
		vu=vu+1
		
	elif(Eu[i]==tesoura and Bar[i]==papel):
		vu=vu+1
		
	elif(Bar[i]==pedra and Eu[i]==tesoura):
		vr=vr+1
		
	elif(Bar[i]==papel and Eu[i]==pedra):
		vr=vr+1
		
	elif(Bar[i]==tesoura and Eu[i]==papel):
		vr=vr+1
		i+=i
	print(size(Eu))
	if(vr > vu):
		print("EUSAPIA")
	elif(vu > vr):
	   print("BARSANULFO")
else:
	print("EMPATE")