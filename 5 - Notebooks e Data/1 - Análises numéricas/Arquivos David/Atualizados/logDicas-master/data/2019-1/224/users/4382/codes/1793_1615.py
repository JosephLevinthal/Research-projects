from numpy import *
v1 = array(eval(input("pontos do jogador 1:")))
v2 = array(eval(input("pontos do jogador 2 :")))
i = 0
soma_1 = 0
soma_2 = 0
valor_1 = 0
valor_2 = 0
while(i<size(v1)):
	if(v1[i]== 1):
	soma_1 = soma_1 + 40
	elif(v1[i]==2):
	soma_1 = soma_1 + 20
	elif(v1[i]==3):
	soma_1 = soma_1 + 10
	elif(v1[i]>=4):
	soma_1 = soma_1 + 0
if(soma_1 == soma_2 ):
	print("EMPATE")
if(soma_1 > soma_2):
	print("JOGADOR UM")
if(soma_2 > soma_1):
	print("JOGADOR DOIS")
	
