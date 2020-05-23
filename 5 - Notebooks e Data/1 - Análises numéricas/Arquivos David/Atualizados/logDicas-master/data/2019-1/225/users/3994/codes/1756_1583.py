from numpy import*
j = str(input("Digite o numero: "))
c=0
i=1
s=""
while(c<len(j)):
	if(i==4):
		i=1
		s= s+"."
	s= s+ j[c]
	i=i+1
	c=c+1
print(s)


