from numpy import*
v = array(eval(input("entrada: ")))
r = size(v)
k= 0
t = 0
s = 0

while(k<r):
	if((r == 1)or(r==2)):
		x = v[s]+"x"
		print(x)
	else:
		
		print(v[s],"x^",t)
	s = s + 1
	k = k + 1
	
	