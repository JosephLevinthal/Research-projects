p=int(input("posicao na corrida: "))
pt=0
while(p!=0):
	if(p==1):
		pt=pt+20
	elif(p==2):
		pt=pt+15
	elif(p==3):
		pt=pt+10
	elif(p==4):
		pt=pt+7
	elif(p==5):
		pt=pt+6
	elif(p==6):
		pt=pt+5
	elif(p==7):
		pt=pt+4
	elif(p==8):
		pt=pt+3
	elif(p==9):
		pt=pt+2
	elif(p==10):
		pt=pt+1
	p=int(input("posicao na corrida: "))
pt=pt
print(pt)