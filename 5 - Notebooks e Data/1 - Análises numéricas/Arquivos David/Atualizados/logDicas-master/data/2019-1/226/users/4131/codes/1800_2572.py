from numpy import*
a = array(eval(input("vai:")))
b = 0 
for y in a:
	if(y%2 !=0):
		b+=1
p = zeros(b, dtype=int)
x=0
g=0
for r in a:
	if(r%2 !=0):
		p[x] = a[g]
		x+=1
	g+=1
print(p)