n=int(input("numero: "))
s=0
i=0
f=n-1
while(i<=f):
	s=s+((-1)**i)*(4/(2*i+1))
	i=i+1
print(round(s,8))