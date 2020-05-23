from numpy import*
s = input("cores:") .split(',')
v = zeros(5 , dtype=int)
p = 0
c = 0
r = 0
l = 0
b = 0
for i in range(size(s)):
	if(s[i] == "P"):
		p = p + 1
	elif(s[i] == "C"):
		c = c+1
	elif(s[i] == "R"):
		r = r+1
	elif(s[i] == "L"):
		l = l+1
	elif(s[i] == "B"):
		b = b +1
v[0] = p
v[1] = c
v[2] = r
v[3] = l
v[4] = b
print(v.max())
print(v)