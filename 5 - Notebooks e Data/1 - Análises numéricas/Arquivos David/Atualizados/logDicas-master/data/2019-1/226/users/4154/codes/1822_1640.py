from numpy import*
a = array(eval(input()))
b = 0
c = 0
for i in a:
	if i%2 != 0:
		b += 1
print(b)
d = zeros(b, dtype=int)
e = 0
for i in a:
	if i%2 != 0:
		d[e] = c
		e += 1
	c+=1

		

print(d)