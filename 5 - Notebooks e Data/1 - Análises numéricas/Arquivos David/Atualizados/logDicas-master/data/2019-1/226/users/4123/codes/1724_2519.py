ht = int(input())
qs = int(input())
qd = int(input())
hs = i = 0

while hs<ht:
	hs += qs
	if hs<ht:
		hs -= qd
	i += 1
print(i)
	