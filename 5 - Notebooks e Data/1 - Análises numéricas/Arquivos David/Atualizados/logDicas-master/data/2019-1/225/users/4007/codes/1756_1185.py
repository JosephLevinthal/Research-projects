from numpy import*
v = array(eval(input("nivel de glicose: ")))
d = 99
i = 0
o = 0
c = 0
t = []
 

while (c < size(v)):
	if (v[i] > d):
		t.append(v[i])
		
	i = i + 1
	c = c + 1
print(size(t))
		