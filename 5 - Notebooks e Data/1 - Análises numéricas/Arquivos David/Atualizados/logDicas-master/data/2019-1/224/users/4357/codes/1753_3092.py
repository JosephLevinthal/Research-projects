v=float(input("digite a letra:"))
d=float(input("digite a letra:"))
total=v+d
i=0
while(i<total):
	v=v+v*d
	d=d+d*v
	i=i+1
print(total)