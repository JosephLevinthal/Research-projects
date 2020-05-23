from numpy import*

v = array(eval(input("vetor:")))
vn = zeros(6, dtype=float)

for e in v:
	if e == 2:
		vn[0] = vn[0] + 1
	elif e == 3:
		vn[1] = vn[1] + 1
	elif e == 4:
		vn[2] = vn[2] + 1
	elif e == 5:
		vn[3] = vn[3] + 1
	elif e == 6:
		vn[4] = vn[4] + 1
	elif e == 7:
		vn[5] = vn[5] + 1
t = sum(vn)
i = 0
for k in vn:
	vn[i] = round((vn[i] * (100/t)),1)
	i = i + 1
print(vn)


