from numpy import*
v = array(eval(input("v: ")))
i = 0
d = 0
r = zeros(d, dtype=int)
for i in range(size(v)):
	if ((v[i] % 2) == 0):
		d = d + 1
		i = i + 1
print(d)

i = 0
e = 0
for i in range(size(v)):
	if ((v[i]%2)==0):
		
		r[i] = v[i] 
		
print(r)