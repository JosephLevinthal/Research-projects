from numpy import*
x=input("Digite a primeira palavra: ").lower()
y=input("Digite a segunda palavra: ").lower()
m=zeros(26)
k=zeros(26)
h=0
n=array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",'t','u','v','x','w','y','z'])
while(len(n)>h):
	f=x.count(n[h])
	m[h]=f
	h=h+1
h=0	
while(len(n)>h):
	j=y.count(n[h])
	k[h]=j
	h=h+1	
h=0
l=zeros(26,dtype=int)
while(len(m)>h):
	l[h]=m[h]-k[h]
	h=h+1

print(l)
h=0
r=26
w=26
while(len(l)>h):
	if(l[h]==0):
		r=r-1
		h=h+1
	else:
		r=r-1

if(r==0):
	print("1")
else:
	print("0")
		
  
		
	
