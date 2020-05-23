n1=int(input("numero 1:"))
n2=int(input("numero 2:"))
p=n1*n2

if((n1*n2)%2==0):
	n=n1+n2
else:
	n=n2-n1
print(n)