from numpy import*
v = array(eval(input('bla bla bla: ')))
i = 0
c = 0
j = 0

while i < size(v):
	if v[i]>=0:
		c += 1
	i +=1
v1 = zeros(c, dtype = int)

i = 0
while i < size(v):
	if v[i]>=0:
		v1[j] = v[i]
		j += 1
	i += 1
print(v1)