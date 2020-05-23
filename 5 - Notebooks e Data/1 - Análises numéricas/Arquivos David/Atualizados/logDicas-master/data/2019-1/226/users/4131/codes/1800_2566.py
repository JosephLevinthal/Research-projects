from numpy import *

presenca=array(eval(input("digite: ")))

cont=zeros(6,dtype=float)

for i in range(size(presenca)):
    
	if presenca[i]==2:
		cont[0]=cont[0]+1 * 100/size(presenca)
	elif ( presenca[i]==3 ):
		cont[1]=cont[1]+1 * 100/size(presenca)
	elif (presenca[i]==4):
		cont[2]=cont[2]+1 * 100/size(presenca)
	elif (presenca[i]==5):
		cont[3]=cont[3]+1 * 100/size(presenca)
	elif (presenca[i]==6):
		cont[4]=cont[4]+1 * 100/size(presenca)
	else:
		(presenca[i]==7)
		cont[5]=cont[5]+1 * 100/size(presenca)

        
for j in range(size(cont)):
    
	cont[0]=round(cont[0],1)
	cont[1]=round(cont[1],1)
	cont[2]=round(cont[2],1)
	cont[3]=round(cont[3],1)
	cont[4]=round(cont[4],1)
	cont[5]=round(cont[5],1)
        
print(cont)