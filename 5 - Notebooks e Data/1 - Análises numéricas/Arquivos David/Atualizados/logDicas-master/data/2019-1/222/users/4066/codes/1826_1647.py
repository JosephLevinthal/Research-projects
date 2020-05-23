from numpy import*

v = array(eval(input("Frequencia: ")), dtype=float)
s = size(v)

ap = 0
for i in v:
	if i >= 70:
		ap = ap + 1
print(ap)
w = zeros(size(v), dtype=int)

z = zeros(ap, dtype=int)

k = 0

for j in range(s):
	if (v[j] >= 70):
		z[k] = j
		k = k + 1

print(z)