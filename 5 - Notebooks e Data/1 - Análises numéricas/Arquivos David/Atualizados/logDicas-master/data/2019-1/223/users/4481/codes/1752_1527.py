qf = int(input('digite qi: '))
ql = int(input('digite ql: '))
pf = float(input('digite pf: '))
pl = float(input('digite pl: '))
x = 0
while(qf>ql) and (pf<pl):
	qf = qf*(pf/100) + ql
	ql = ql*(pl/100) + ql
	x = x +1

print(x)