qv = int(input())
ql = int(input())
pv = float(input())
pl = float(input())
gv = qv
gl = ql
t = 0
while(gl < 2 * gv):
	gl = gl + ((gl * pl) / 100)
	gv = gv + ((gv * pv) / 100)
	t = t + 1
print(t)