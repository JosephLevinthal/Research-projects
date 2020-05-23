from numpy import*

x = array(eval(input("nnn:")))

f = size(x)
z = ""
d = " + "
j = "x"
for i in range(size(x)):
	f = f -1
	p = x[i]
	z = z + str(p) + "x^" + str(f) + d
	if f == 0:
		z = z  j 
print(z)
		