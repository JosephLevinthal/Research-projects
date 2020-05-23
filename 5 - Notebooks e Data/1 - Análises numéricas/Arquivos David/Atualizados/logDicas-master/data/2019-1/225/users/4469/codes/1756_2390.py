from numpy import*

p = array(eval(input()))
f = array(eval(input()))

i = 0
while(i < 12):
	if(max(p) == p[i]):
		print(i + 1)
		break
	i = i + 1