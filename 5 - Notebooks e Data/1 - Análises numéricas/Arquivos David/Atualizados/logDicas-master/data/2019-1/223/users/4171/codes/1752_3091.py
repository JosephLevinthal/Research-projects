m = input().upper()

n = m
r = 0
c = 0


while m != "X":
	
	if n == "V":
		r += 3
	elif n == "E":
		r += 1
	elif n == "D":
		r += 0
	if n == "X":
		break
	c += 1
	
	m = n
	
pmaxima = c*3
ptime = (r/pmaxima)
ptime = round(ptime,2)
print(ptime)