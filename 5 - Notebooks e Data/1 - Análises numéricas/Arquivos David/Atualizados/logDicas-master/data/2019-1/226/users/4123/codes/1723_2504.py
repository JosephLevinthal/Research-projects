qv = float(input())
ql = float(input())
pv = int(input())
pl = int(input())
i = 0

while ql<2*qv:
	qv+=qv*pv/100
	ql+=ql*pl/100
	i+=1
print(i)
