from numpy import*
v = array(eval(input("vetor: ")))
t = 0
a = 0
n = size(v)
while (t < n):
	if v[t]<0:
		a = a + 1
	t = t + 1
v1 = zeros(n-a, dtype=int)
t = 0
i = 0
while (t < n):
	if v[t]>=0:
		v1[i] = v[t]
		i = i + 1
		t = t + 1
	else:
		t = t+1
print(v1)