n= int(input("insira um numero natural: "))
s=n
while s!=1:
	if s%2==0:
		s=s//2
	else:
		s=s*3+1
	print(s)