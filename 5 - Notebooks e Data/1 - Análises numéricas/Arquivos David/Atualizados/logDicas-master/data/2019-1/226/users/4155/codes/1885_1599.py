from numpy import*
v = array(eval(input("v: ")))
i = 0
d = 0
e = (v[i]*15)/100
for i in range(size(v)):
	if (v[i]> 80.0):
		d =  v[i] - ((v[i]*15)/100) + d
	elif (v[i] <= 80.0):
		d = v[i] + d
	i = i + 1
print(round(d, 2))