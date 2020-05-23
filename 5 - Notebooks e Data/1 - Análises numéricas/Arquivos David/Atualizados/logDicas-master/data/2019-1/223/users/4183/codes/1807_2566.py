from numpy import *
v = array(eval(input("Digite: ")))
vf = array(zeros(6,dtype=int))
vr = array(zeros(6,dtype=float))
for i in range(size(v)):
	if (v[i] == 2):
		vf[0] = vf[0] + 1
	elif (v[i] == 3):
		vf[1] = vf[1] + 1
	elif (v[i] == 4):
		vf[2] = vf[2] + 1
	elif (v[i] == 5):
		vf[3] = vf[3] + 1
	elif (v[i] == 6):
		vf[4] = vf[4] + 1
	elif (v[i] == 7):
		vf[5] = vf[5] + 1
for i in range(size(vf)):
	vr[i] = round((vf[i] / size(v) * 100),1)
print(vr)