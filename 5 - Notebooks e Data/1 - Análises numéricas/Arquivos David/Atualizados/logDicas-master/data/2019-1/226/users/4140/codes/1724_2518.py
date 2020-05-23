n=int(input())

if(n%2==0):
	n=n//2
	print(n)
	while(n!=1):
		if(n%2==0):
			n=n//2
			print(n)
		else:
			n=n*3+1
			print(n)
	
	
else:
	n=n*3+1
	print(n)
	while(n!=1):
		if(n%2==0):
			n=n//2
			print(n)
		else:
			n=n*3+1
			print(n)
	