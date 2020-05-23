from numpy import*
es=input("qual o estado:").split(",")
cont=zeros(5,dtype=int)
for i in range (size(es)):
	if(es[i]=="AM"):
		cont[0]=cont[0]+1
	if(es[i]=="AC"):
		cont[1]==cont[1]+1
	if(es[i]=="RR"):
		cont[2]=cont[2]+1
	if(es[i]=="RO"):
		cont[3]=cont[3]+1
	if(es[i]=="PA"):
		cont[4]=cont[4]+1
print(cont)