from numpy import*

s= eval(input("Insira as opcoes"))
cont= zeros(3, dtype=int)

for i in range(size(s)):
	if(s[i]== "TV"):
		cont[0]+=1
	elif(s[i]== "NETFLIX"):
		cont[1]+=1
	elif(s[i]== "YOUTUBE"):
		cont[2]+=1
print(cont)