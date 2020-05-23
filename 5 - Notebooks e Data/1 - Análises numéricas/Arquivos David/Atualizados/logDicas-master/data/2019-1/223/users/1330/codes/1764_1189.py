a = input()
x = a.replace(" ","")
i = 0
j = -1
while(i<len(x)):
	if(x[i]==x[j]):
		i = i + 1
		j = j -1
	print(x.upper())
	print(1)
	#elif(x[i]=!x[j]):
	#	print(x.upper())
	#	print(0)