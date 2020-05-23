n = int(input("numero inteiro: "))
d = 1
i=0
while(d<=n):
	if((n%d)==0):
		print(d)
		d= d+1
		i = i+1
	else:
		#i=i+1
		d=d+1
print(i,"divisores")