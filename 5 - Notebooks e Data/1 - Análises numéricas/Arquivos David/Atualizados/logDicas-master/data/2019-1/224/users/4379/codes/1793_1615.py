from numpy import *
v1=array(eval(input("digite o vetor: ")))
v2=array(eval(input("digite o vetor: ")))
cont=0
soma1=0
soma2=0
while(cont<size(v1)):
	if(v1[cont]==1):
		soma1=soma1+40
	elif(v1[cont]==2):
		soma1=soma1+20
	elif(v1[cont]==3):
		soma1=soma1+10
	if(v2[cont]==1):
		soma2=soma2+40
	elif(v2[cont]==2):
		 soma2=soma2+20
	elif(v2[cont]==3):
		 soma2=soma2+10
	cont=cont+1
if(soma1>soma2):
	print("JOGADOR UM")
elif(soma1==soma2):
	print("EMPATE")
else:
	print("JOGADOR DOIS")
	


	
	
	

	
	
