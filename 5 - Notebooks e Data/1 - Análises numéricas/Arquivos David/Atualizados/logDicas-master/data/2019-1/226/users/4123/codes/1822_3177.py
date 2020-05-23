from numpy import*
s = input()
a = e = i = o = u = 0
for x in s:
	if x == "a":
		a += 1
	elif x == "e":
		e += 1
	elif x == "i":
		i += 1
	elif x == "o":
		o += 1
	elif x == "u":
		u += 1
print("a:",a)
print("e:",e)
print("i:",i)
print("o:",o)
print("u:",u)