qv = int(input())
ql = int(input())
pv = float(input())
pl = float(input())

t = 0

while(ql < 2 * qv):
	ql = ql + ((ql * pl) / 100)
	qv = qv + ((qv * pv) / 100)
	t = t + 1
	
print(t)