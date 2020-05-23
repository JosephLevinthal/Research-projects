n = int(input(""))
cont=0
x=1
y=0
res1=0
res=12**0.5
res2=0
while(cont!=n):
	if(cont==0):
		res2=res * (1/(x * (3**y)))
	else:
		res2 = res * 1/(x * 3**y)
	if(cont%2 !=0):
		res2= res2 * (-1)
	res1=res2+res1
	x+=2
	y+=1						  
	cont+=1
print(round(res1,8))	