n = input("leia a string: ")
j =''
for i in range(len(n)):
	if(n[i].upper()!="A"):
		j = j + n[i]
	elif(n[i].upper=="A" ):
		j = j
print(j)
	