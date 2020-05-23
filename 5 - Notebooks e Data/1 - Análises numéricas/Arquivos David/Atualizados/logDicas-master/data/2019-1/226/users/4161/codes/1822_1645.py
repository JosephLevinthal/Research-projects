from numpy import*
v = array(eval(input("vetor: ")))
a = 0
for x in v:
	if x>= 2000:
		a = a + 1
print(a)
v1 = zeros(a, dtype=int)
t = 0
b = 0
for x in v:
	if t < a:
		if x >=2000:
			v1[t] = b
			t = t + 1
		b = b + 1
print(v1)