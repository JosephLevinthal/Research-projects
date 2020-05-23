from numpy import*
gols=array(eval(input("GOl:")))
golsc=array(eval(input("GOls sofridos:")))
i=3
cont=zeros(i, dtype=int)
for n in range(size(gols)):
	if(gols[n]>golsc[n]):
		cont[0]=1+cont[0]
	elif(gols[n]<golsc[n]):
		cont[2]=1+cont[2]
	elif(gols[n]==golsc[n]):
		cont[1]=1+cont[1]
print(cont) 