from numpy import*
v1 = array(eval(input("N: ")))
v2 = array(eval(input("N: ")))
v = int(input("Digite: "))
r = array(zeros(3, dtype =int))
for i in range(size(v1)):
	if(v1[i] < 5):
		r[1] = r[1]+1
	elif(v2[i] < (v * 75 // 100)):
		r[2] = r[2]+1
	else:
		r[0] = r[0]+1
print(r)