x= int(input("tecle qualquer numero para iniciar:"))

soma=0

while (x != 0):
	x=int(input("posicao:"))
	if(x<0):
		x=x*(-1)
	if(x==1 and x!=0):
		soma=soma+25
	elif(x==2 and x!=0):
		soma=soma+18
	elif(x==3):
		soma=(soma+12)
	elif(x >= 4 and x <= 10 and x!=0):
		soma=(soma+14-x)
	else:
		14
		
print(round(soma-soma*0.24))