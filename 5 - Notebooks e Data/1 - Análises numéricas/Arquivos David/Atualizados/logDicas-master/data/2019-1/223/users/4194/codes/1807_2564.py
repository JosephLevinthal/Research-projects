from numpy import*
p1 = array(eval(input("N: ")))
p2 = array(eval(input("N: ")))
v = array(zeros(3,dtype=int))
for i in range(size(p1)):
	if(p1[i] > p2[i]):
		v[0] = v[0] + 1
	elif(p1[i] == p2[i]):
		v[1] = v[1] + 1
	elif(p1[i] < p2[i]):
		v[2] = v[2] + 1
print(v)