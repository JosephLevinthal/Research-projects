from numpy import*
v = array(eval(input("digite as notas: ")))
a = size(v)
b = 0
for i in range(a):
	if(v[i] >= 5 ):
		b = b + 1
		
print(b)
k = zeros(b, dtype=int)
h = 0
for j in range(a):
	if(v[j] >= 5):
		k[h] = j
		h = h + 1
print(k)
	