from numpy import*
v = array(eval(input("vetor: ")))
n = size(v)
r = zeros(3, dtype=int)
t = 0
ne = 0
y = 0
for x in v:
	if x.upper() == "TV":
		t = t + 1
	elif x.upper() == "NETFLIX":
		ne = ne + 1
	elif x.upper() == "YOUTUBE":
		y = y + 1
r[0] = t
r[1] = ne
r[2] = y
print(r)