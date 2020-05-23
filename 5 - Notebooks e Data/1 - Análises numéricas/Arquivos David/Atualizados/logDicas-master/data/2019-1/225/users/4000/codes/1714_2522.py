n = int(input("numero inteiro: "))
c= 1.5
e=0
d=0
i=0
while(n<c and n>0):
	if(c==0):
		e = e*2
	else:
		e = e *(1 +(i/d))
	i = i+1
	d = d+2
	c= c+1
print(round(e,2))
	