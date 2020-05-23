from numpy import *
t1 = array(eval(input("Dgite: ")))
t2 = array(eval(input("Dgite: ")))
r = array(zeros(3,dtype=int))
for i in range(size(t1)):
	if (t1[i] > t2[i]):
		r[0] = r[0] + 1
	elif (t1[i] == t2[i]):
		r[1] = r[1] + 1
	elif (t1[i] < t2[i]):
		r[2] = r[2] + 1
print(r)