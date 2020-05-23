n= int(input("numero de repeticoes: "))
s=0
i=0
while(n>i):
	s= s + 4/(2*i+1)*(-1)**i
	i=i+1
print(round(s,8))