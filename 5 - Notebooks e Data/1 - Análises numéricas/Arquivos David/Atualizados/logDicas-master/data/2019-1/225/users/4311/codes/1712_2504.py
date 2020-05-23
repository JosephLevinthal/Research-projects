qv = int(input())
ql = int(input())
pv = float(input())
pl = float(input())

cql = ql
cqv = qv
t = 0

while(cql < 2 * cqv):
	cql = cql + ((cql * pl) / 100)
	cqv = cqv + ((cqv * pv) / 100)
	t = t + 1
	
print(t)