from numpy import*

m = array(eval(input("Gols marcados: ")))
s = array(eval(input("Gols sofridos: ")))

a = zeros(3, dtype=int)

v = 0
d = 0
e = 0

for x in range(size(m)):
	if(m[x] > s[x]):
		v = v + 1
	elif(m[x]< s[x]):
		d = d + 1
	else:
		e = e + 1
a[0] = v
a[1] = e
a[2] = d

print(a)

	
		