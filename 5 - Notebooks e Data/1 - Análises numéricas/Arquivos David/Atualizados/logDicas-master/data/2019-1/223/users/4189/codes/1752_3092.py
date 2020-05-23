jogo=input("jogo:").upper()
pont=0
porc=0
while(jogo!="X"):
	if(jogo=="V"):
	   pont=pont+3/
	elif(jogo=="E"):
	   pont=pont+2/
	elif(jogo=="D"):
	   pont=pont+1/
	else:
		pont=pont+0
	jogo=input("jogo:").upper()
	
print(round(porc,2))