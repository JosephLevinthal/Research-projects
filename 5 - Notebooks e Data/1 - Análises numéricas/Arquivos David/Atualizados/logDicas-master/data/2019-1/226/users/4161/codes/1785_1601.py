from numpy import*
v = array(eval(input("tempos de chegada: ")))
mn = min(v)
n = size(v)
t = 0
while t < n:
	if v[t] == mn:
		i = t
		t = n
	t = t + 1
print(i)