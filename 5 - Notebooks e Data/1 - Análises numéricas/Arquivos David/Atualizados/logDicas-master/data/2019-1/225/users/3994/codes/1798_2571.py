b = input("s:")
j=''
for i in range (len(b)):
	if(b[i].upper()!= "A"):
		j= j+ b[i]
	elif(b[i].upper()=="A"):
		j=j
print(j)