from numpy import *
p = int(input("s: "))
mt = ones((p,p), dtype=int)

for x in range(p):
	for y in range(p):
		if(x<y):
			mt[x,y]= x + 1
		elif(y>x):
			mt[x,y] = y + 1
		else:
			mt[x,y] = y + 1
print(mt)