from numpy import*
a = array(eval(input("")))
i=0
g=0
while(i < size(a)):
	if(a[i] > 99):
		g +=1
		print(i)
	i += 1
print(g)