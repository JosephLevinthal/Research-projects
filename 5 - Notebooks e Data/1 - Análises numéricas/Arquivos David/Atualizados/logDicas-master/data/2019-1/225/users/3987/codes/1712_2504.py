qv = int(input(":"))
ql = int(input(":"))
pv = float(input(":"))
pl = float(input(":"))

i = 0

while(ql < 2*qv):
	qv = qv + ((qv * pv)/100)
	ql = ql + ((ql * pl)/100)
	i = i + 1
print(i)
	


