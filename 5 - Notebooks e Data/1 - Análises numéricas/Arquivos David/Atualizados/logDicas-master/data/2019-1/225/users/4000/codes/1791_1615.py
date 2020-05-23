from numpy import*
v1 = array(eval(input("Aneis acertados pelo primeiro jogador: ")))
v2 = array(eval(input("Aneis acertados pelo segundo jogador: ")))
i =0
a1 = 40
a2 = 20
a3 = 10
a4 = 0
va1 = 0 #pontuaçao do jogador 1 
va2= 0 #pontuaçao do jogador 2
while(i<size(v1)):
	if(v1[i]==a1 and v2[i]==a1):
		a1 = a1 + 1
		
	elif(v1[i]==a2 and v2[i]==a2):
		a2 = a2 +1
	elif(v1[i]==a3 and v2[i]==a3):
		a3 = a3 +1
	else:
		a4 = a4 +1
	i = i+1
	
	if(va1>va2):
		print("JOGADOR UM")
	elif(va2>va1):
		print("JOGADOR DOIS")
	else:
		print("EMPATE")
	
	
		
	
	


