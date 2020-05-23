n=int(input("numero:"))
t=0  #quantidade de divisores
x=1  #numero que esta dividindo
while(x<=n ):
	
	if(n%x==0):
		t+=1
		print(x)
	x+=1
if(t==1):
	i="divisor"
else:
	i="divisores"
print(t,i)