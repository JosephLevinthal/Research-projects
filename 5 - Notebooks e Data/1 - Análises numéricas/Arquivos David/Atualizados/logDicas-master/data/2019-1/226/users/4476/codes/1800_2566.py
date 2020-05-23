from numpy import *
v = array(eval(input("digite: ")))

vc = zeros(6, dtype=float)

for i in v:
	if i == 2:
		vc[0] = vc[0] + 1
	elif i == 3:
		vc[1] = vc[1] + 1
	elif i == 4:
		vc[2] = vc[2] + 1
	elif i == 5:
		vc[3] = vc[3] + 1
	elif i == 6:
		vc[4] = vc[4] + 1
	elif i == 7:
		vc[5] = vc[5] + 1
for i in range(size(vc)):
	vc[i] = round((vc[i]*100)/size(v), 1)
print(vc)
