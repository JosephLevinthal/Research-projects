from numpy import*
a = array(eval(input()))
c = zeros(6)
for i in range(size(a)):
	if a[i] == 2:
		c[0] += 1
	elif a[i] == 3:
		c[1] += 1
	elif a[i] == 4:
		c[2] += 1
	elif a[i] == 5:
		c[3] += 1
	elif a[i] == 6:
		c[4] += 1
	elif a[i] == 7:
		c[5] += 1
for z in range(size(c)):
	c[z] = (c[z]/size(a))*100
	c[z] = round(c[z],1)
print(c)

