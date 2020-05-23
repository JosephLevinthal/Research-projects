qiv = int(input())
qil = int(input())
pmv = int(input())
pml = int(input())

dias = 0
v = qiv
l = qil
while(v>l/2):
	totalv = v * (pmv/100)
	totall = l * (pml/100)
	v = totalv + v
	l = totall + l
	dias = dias + 1

print(dias)