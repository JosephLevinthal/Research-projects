qi = int(input('qi: '))
ql = int(input('ql: '))
pv = float(input('pv: '))
pl = float(input('pl: '))

c = 0

while (qi*2>ql):
	qi = qi + qi*(pv/100)
	ql = ql + ql*(pl/100)
	c = c+1
print(c)
	