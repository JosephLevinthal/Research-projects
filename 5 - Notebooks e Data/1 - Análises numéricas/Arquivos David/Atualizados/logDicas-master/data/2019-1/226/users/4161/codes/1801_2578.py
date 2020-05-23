from numpy import*
v1 = array(eval(input("bla bla: ")))
n = 0
for x in v1:
	if x%2 == 0:
		n = n + 1
v2 = zeros(n, dtype=int)
i = 0
for x in v1:
	if x%2 == 0:
		v2[i] = x
		i = i + 1
print(v2)