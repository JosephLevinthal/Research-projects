x = input()
i = 0
j = ""
while i+3<=len(x):
	j+= x[i]
	j+= x[i+1]
	j+= x[i+2]
	if i+3<len(x):
		j+= "."
	i+=3
print(j)