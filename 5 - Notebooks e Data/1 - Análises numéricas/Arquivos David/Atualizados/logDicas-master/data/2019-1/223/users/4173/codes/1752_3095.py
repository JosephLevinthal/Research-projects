v = input().upper()
a = 0
c = 0
f = 0
while (v == "V") or (v == "E") or (v == "D"):
	if (v == "V"):
		a += 3
	elif(v == "E"):
		c += 2
	elif(v == "D"):
		f += 1
	v = input().upper()
print(a)
print(c)
print(f)