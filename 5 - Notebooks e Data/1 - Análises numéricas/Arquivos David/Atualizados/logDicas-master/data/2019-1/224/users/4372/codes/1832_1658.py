from numpy import*
a=input("digite os paises: ").upper().split(',')
cont=zeros(5,dtype=int)
for i in range(size(a)):
	if(a[i]=="CHN"):
		cont[0]=cont[0]+1
	if(a[i]=="JPN"):
		cont[1]=cont[1]+1
	if(a[i]=="KOR"):
		cont[2]=cont[2]+1
	if(a[i]=="MGL"):
		cont[3]=cont[3]+1
	if(a[i]=="THA"):
		cont[4]=cont[4]+1
print(max(cont))
print(cont)