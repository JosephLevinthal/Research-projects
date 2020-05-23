x=input("Digite um numero mulitplo de 3: ")
y="."
z=3
r=0
d=""
while(len(x)>z):
	d=d+(x[r:z]+y)
	r=r+3
	z=z+3
	f=d+x[r:z]

if(len(x)==3):
	f=x
print(f)	
	
	
	

 
	