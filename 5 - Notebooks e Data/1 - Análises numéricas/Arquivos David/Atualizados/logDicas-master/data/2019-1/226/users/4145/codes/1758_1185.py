from numpy import*
v =array(eval(input("pessoas: ")))
i=0
g=0
while(i<size(v)):
	if(v[i]>99):
		g=g+1
		print(i)
	i=i+1
print(g)	