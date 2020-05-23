n = input("digite: ")
i=0
cont=""

while(i<len(n)):
	if((i+1)%3==0 and i<len(n)-1):
		cont= cont + n[i] + "."
	else:
		cont= cont + n[i]
	i= i+1
print(cont)