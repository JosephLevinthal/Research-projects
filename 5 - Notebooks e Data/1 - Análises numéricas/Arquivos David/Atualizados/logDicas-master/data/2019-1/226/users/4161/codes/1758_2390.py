from numpy import*
vp = array(eval(input("vai que e tua: ")))
vf = array(eval(input("vai que e tua/2: ")))
v = zeros(12, dtype=int)
t = 0 
n = 12 
while t < n:
	v[t] = vp[t] - vf[t]
	t = t + 1
t = 0
m = max(v)
while t < n:
	if m == v[t]:
		print(t + 1)
		t = n
	else:
		t = t + 1