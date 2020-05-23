from numpy import* 
cont= zeros(3, dtype=int)
v1= array(eval(input("Insira o numero de gols feitos:")))
v2= array(eval(input("Insira o numero de gols levados:")))

for i in range(size(v1)) and range(size(v2)):
	if(v1[i]>v2[i]):
		cont[0]=cont[0]+1
	elif(v1[i]==v2[i]):
		cont[1]=cont[1]+1
	elif(v1[i])<v2[i]:
		cont[2]=cont[2]+1
print(cont)