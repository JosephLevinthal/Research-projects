n=input("numero: ")

i = 0
n1 = ""
while (i < len(n)):
	if ((i+1)%3 == 0) and ((i+1) != len(n)):
		n1 += n[i] + "."
	else:
		n1 = n1 + n[i]
		
	i +=1
	
print(n1)