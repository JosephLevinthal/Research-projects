x=int(input("digite um numero: "))
j=0
z=0
g=0
f=0
while(x!=0):
	if(x%2==0):
		z=z+1
		j=j+x
		x=int(input("Digite um numero: "))
	  
	else:
		g=g+x
		f=f+1
		x=int(input("Digite um numero: "))

if(z!=0):
   print(round(j/z,2))
else:
	print(round(j/1,2))

if(f!=0):	
   print(round(g/f,2))
else:
	print(round(g/1,2))
		