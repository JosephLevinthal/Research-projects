from numpy import*

v = array(eval(input("vetor: ")))

i = 0        #contador 1
h = 0        #contador 2
x = 0        #tamanho 1
q = 0        #tamanho 2

while i < size(v):
	if v[i] >= 0:
		x = x + 1
	else:
		x = x
	i = i + 1
x = arange(x)
while h < size(v):
	if v[h] >= 0:
		x[q] = v[h]
		q = q + 1
		h = h + 1
	else:
		h = h + 1
print(x)