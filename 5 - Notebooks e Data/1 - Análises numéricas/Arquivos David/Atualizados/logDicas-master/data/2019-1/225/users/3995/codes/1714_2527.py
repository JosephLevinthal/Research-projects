n=int(input("numero:"))
t=0
x=1
h=0
while(x<n):
	if(n%x==0):
		t+=1
		print(x)
		h+=x
	
	x+=1

if(h==n):
	print("PERFEITO")
else:
	print("NAO PERFEITO")