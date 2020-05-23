from numpy import*
et=input("tipos de etnia:").split(",")
cont=zeros(5,dtype=int)
for i in range (size(et)):
	if(et[i]=="B"):
		cont[0]=cont[0]+1
	if(et[i]=="PA"):
		cont[1]=cont[1]+1
	if(et[i]=="PR"):
		cont[2]=cont[2]+1
	if(et[i]=="A"):
		cont[3]=cont[3]+1
	if(et[i]=="I"):
		cont[4]=cont[4]+1
print(max(cont))
print(cont)
	
