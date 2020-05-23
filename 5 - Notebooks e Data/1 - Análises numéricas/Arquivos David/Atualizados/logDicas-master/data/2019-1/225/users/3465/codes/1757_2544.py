from numpy import *
p = array(eval(input("")))
a = 0
b = 0
c = 0
for i in p:
	if i>=10:
		a+=1
	elif i>=5 and i<10:
		b+=1
	else:
		c+=1
print(a)
print(b)
print(c)