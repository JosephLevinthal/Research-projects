a=int(input("virus "))
b=int(input("leucocitos "))
c=int(input("Percentual virus"))
d=int(input("Percentual leucocitos"))
s=a#virus
v=b#leucocitos
q=0

while(v<2*s):
	s=s+s*c/100
	v=v+v*d/100
	q=q+1

print(q)