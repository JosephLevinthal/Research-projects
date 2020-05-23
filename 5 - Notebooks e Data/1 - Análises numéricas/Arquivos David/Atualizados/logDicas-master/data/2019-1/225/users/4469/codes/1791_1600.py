from numpy import*

v = array(eval(input()))

s = 0

i = 0
while(i < size(v)):
	if(v[i] > 80.0):
		v[i] = v[i] - ((v[i] * 15) / 100)
	
	s = s + v[i]
	i = i + 1

print(round(s, 2))