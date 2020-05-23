n=int(input("digite um numero: "))
i=0
d=1
while(d<=n):
	if((n%d)==0):
		print(d)
		d=d+1
		i=i+1
	else:
		d=d+1
print(i,"divisores")
	

	
	