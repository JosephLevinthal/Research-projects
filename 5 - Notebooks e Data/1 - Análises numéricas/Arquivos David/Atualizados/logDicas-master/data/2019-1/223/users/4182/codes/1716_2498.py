na = int(input())
nb = int(input())
pa = float(input())
pb = float(input())

num = 0

while (na <= nb):
	c1 = na*pa/100
	na = na + c1
	c2 = nb*pb/100
	nb = nb + c2
	num += 1
print(num)