from numpy import*
v = input("Estados: ").split(',')

ac = 0
am = 0
pa = 0
ro = 0
rr = 0
a = zeros(5, dtype=int)
for i in range(size(v)):
	if (v[i] == "AC"):
		ac = ac + 1
	elif (v[i] == "AM"):
		am = am + 1
	elif (v[i] == "PA"):
		pa = pa + 1
	elif (v[i] == "RO"):
		ro = ro + 1
	elif (v[i] == "RR"):
		rr = rr + 1
a[0] = ac
a[1] = am
a[2] = pa
a[3] = ro
a[4] = rr
print(max(a))
print(a)