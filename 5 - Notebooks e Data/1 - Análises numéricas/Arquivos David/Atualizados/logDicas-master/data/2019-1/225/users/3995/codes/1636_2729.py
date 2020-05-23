n1=int(input("numero: "))
n2=int(input("numero: "))
k=(n1*n2)%2
if(k==0):
	print(n1+n2)
else:
	print(abs(n1-n2))