x = input("q: ")
j = " "
for i in range(len(x)):
	if(x[i].upper()!="A"):
		j = j + x[i]
	elif(x[i].upper()=="A"):
		j = j
print(j)