a=int(input("numero habitantes A: "))
b=int(input("numero habitantes B: "))
c=float(input("crescimento A: "))
d=float(input("crescimento B: "))
anos=0
while(a<b):
	a=a+a*(c/100)
	b=b+b*(d/100)
	anos=anos+1
print(anos)	
	
