from numpy import*

d = array(eval(input("vetor dos indices de glicose: ")))

i = 0  #contador 1
e = 0  #contador 2
r = 99 #risco de diabetes

while i < size(d):
	if d[i] <= r:
		i = i + 1
	else:
		print(i)
		i = i + 1
		e = e + 1
print(e)