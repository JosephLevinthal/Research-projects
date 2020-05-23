a=int(input("valor de a: "))
b=int(input("valor de b: "))

pd=(a*b)%2

if(pd==0):
	print(a+b)
else:
	print(b-a)