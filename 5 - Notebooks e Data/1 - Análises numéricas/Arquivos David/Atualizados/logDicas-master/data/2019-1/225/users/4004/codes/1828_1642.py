from numpy import*
x = array(eval(input("turmas: ")))

t = 0
j = 0
k = 0

for i in x:
	if i % 5 == 0:
		t = t + 1
	else:
		t = t
print(t)
y = zeros(t, dtype=int)
for i in x:
	if i % 5 == 0:
		y[k] = j
		j = j + 1
		k = k + 1
	else:
		j = j + 1
print(y)