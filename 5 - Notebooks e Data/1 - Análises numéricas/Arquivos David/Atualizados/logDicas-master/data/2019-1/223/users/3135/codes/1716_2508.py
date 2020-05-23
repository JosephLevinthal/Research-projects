n= int(input("Insira o valor de N termo:"))
cont=0
res=0
res1=0
res2=0
x1=2
x2=3
x3=4
while(cont!=n):
	if(cont==0):
		res=3
	else:
		res= 4/(x1*x2*x3)
	if(cont%2==0 and cont>0):
		res=res*(-1)
	res1= res+ res1
	if(cont>0):
		x1=x1+2
		x2=x2+2
		x3=x3+2
	cont+=1

print(round(res1,8))