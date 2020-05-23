n = int(input("numero inteiro: "))
d = 1
i=0
s=0
while(d<n):
	if((n%d)==0):
		print(d)
		i = i+1
		s=  s+d
		d= d+1
	else:
		#i=i+1
		d=d+1
		s=s+0
if(s==n):
	print("PERFEITO")
else:
	print("NAO PERFEITO")