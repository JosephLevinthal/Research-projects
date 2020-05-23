from numpy import*
f=array(eval(input("numero de faltas por dia da semana: ")))
cont=zeros(6, dtype=int)

for i in range(size(f)):
	if(f[i]==2):
		cont[0]=cont[0]+1
	if(f[i]==3):
		cont[1]=cont[1]+1
	if(f[i]==4):
		cont[2]=cont[2]+1
	if(f[i]==5):
		cont[3]=cont[3]+1
	if(f[i]==6):
		cont[4]=cont[4]+1
	if(f[i]==7):
		cont[5]=cont[5]+1
vp=zeros(6,dtype=float)
for i in range (size(vp)):
	vp[i]=round((cont[i]/(size(f)))*100, 1)
print(vp)