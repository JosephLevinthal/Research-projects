from numpy import*

v=array(eval(input()))

while (size(v) > 1):
	a=0
	for elemento in v:
		if (elemento < 7) and (elemento >=5):
			a=a+1
	print(a)
	v=array(eval(input()))	