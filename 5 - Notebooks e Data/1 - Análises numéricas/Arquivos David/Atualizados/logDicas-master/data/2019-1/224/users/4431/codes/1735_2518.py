x=int(input("Digite um numero: "))
while(x>1):
	if(x%2==0):
		x=x//2
		print(x)
	else:
		x=(x*3)+1
		print(x)
		