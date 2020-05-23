p=int(input("posicao de chegada: "))
i=0
while(p!=0):
	if(p==1):
		i=20
	elif(p==2):
		i=15
	elif(p==3):
		i=10
	elif(p==4)or(p==5)or(p==6)or(p==7)or(p==8)or(p==9)or(p==10):
		i=11-p
	elif(p>10):
		i=0
	i=i
print(i)
		
