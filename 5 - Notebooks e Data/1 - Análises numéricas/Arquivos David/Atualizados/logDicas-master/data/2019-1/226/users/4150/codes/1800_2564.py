from numpy import* 

v1 = array(eval(input("digite: ")))
v2 = array(eval(input("digite: ")))

x = zeros(3,dtype = int)

for i in range(size(v1)):
	if v1[i] > v2[i]:
		x[0] = x[0] + 1
	elif v1[i] == v2[i]:
		x[1] = x[1] + 1
	elif v1[i] < v2[i]:
		x[2] = x[2]+ 1
print(x)