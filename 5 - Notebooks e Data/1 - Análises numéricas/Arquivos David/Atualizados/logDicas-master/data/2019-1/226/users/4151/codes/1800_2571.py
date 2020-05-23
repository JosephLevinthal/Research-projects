string=input()


saida=""

for i in range(len(string)): 
	if(string[i].upper()!="A"):
		saida=saida+string[i]
print(saida)
		