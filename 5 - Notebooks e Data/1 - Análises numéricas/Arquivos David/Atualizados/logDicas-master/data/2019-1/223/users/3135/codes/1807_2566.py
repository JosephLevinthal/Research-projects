from numpy import*
cont=zeros(6, dtype=float)

v= array(eval(input("Insira o bla bla bla:")))

for i in range(size(v)):
	if(v[i]==2):
		cont[0]=cont[0]+1
	elif(v[i]==3):
		cont[1]=cont[1]+1
	elif(v[i]==4):
		cont[2]=cont[2]+1
	elif(v[i]==5):
		cont[3]=cont[3]+1
	elif(v[i]==6):
		cont[4]=cont[4]+1
	elif(v[i]==7):
		cont[5]=cont[5]+1			
d=sum(cont)

for a in range(size(cont)):
	cont[a]=(cont[a]/d) *100
	cont[a]=round(cont[a],1)
print(cont)