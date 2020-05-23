from numpy import*
v = array(eval(input("letras: ")))
j = ""
n = size(v)
for t in range(n):
	j = j + v[t]
a = min(j)
b = a
for x in j:
	j = j.replace(b, "")
	b = min(j)
	a = a + b
print(a)

