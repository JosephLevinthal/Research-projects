virus=int(input("virus:"))
leucocitos=int(input("leucocitos:"))
mv=int(input("mv:"))
ml=int(input("ml:"))
dias=0
v=virus
l=leucocitos
while(l/2<v):
	v=v+(v*mv)/100
	l=l+(l*ml)/100
	dias=dias+1
print(dias)