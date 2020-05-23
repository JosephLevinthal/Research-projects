from numpy import*

a = array(eval(input("gols do time A:")))
b = array(eval(input("gols do time B:")))
va = 0
e = 0
d = 0 
v = zeros(3 , dtype = int)
for i in range(size(a)):
	if(a[i] > b[i]):
		va = va + 1
	elif(a[i] == b[i]):
		e = e + 1
	elif(a[i] < b[i]):
		d = d + 1
v[0] = va
v[1] = e
v[2] = d

print(v)