from numpy import * 
freq = array(eval(input("digite as frequencias: ")))
ap = 0
rep = 0
for i in freq:
	if(i >= 70):
		ap = ap + 1
	else:
		rep = rep + 1
print(ap)
z = zeros(ap, dtype = int)
b = 0
v = 0
for j in freq:
	if(j >= 70):
		z[b] = v
		b = b + 1
	v = v + 1
print(z)
		
	