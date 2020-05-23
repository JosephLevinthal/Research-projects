x=int(input("Digite um numero: "))
y=int(input("Digite um numero: "))
j=1
f=1
g=0
b=0
while(j<x):
	if(x%j==0):
		g=j+g
		j=j+1		
	else:
		j=j+1
		
while(f<y):
	if(y%f==0):
		b=f+b
		f=f+1		
	else:
		f=f+1	
		
print(g)
print(b)
if(g==y)and(b==x):
	print("AMIGOS")
else:
	print("NAO AMIGOS")