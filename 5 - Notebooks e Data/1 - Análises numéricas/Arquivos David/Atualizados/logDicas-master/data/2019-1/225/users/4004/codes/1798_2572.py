from numpy import*
x = array(eval(input("vetor: ")))
y = x
t = 0

for i in x:
	if (i % 2) == 0:
		t = t
	else:
		t = t + 1
z = zeros(t, dtype=int)
k = 0
for j in y:
	if (j % 2) != 0:
		z[k] = y[j]
		k = k + 1
print(z)