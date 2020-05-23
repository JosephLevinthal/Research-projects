from numpy import *
string = input("digite a string: ")
v = string.split(",")
a,p,m,s,r = 0,0,0,0,0
for i in v:
	if(i == "AM"):
		a = a + 1
	if(i == "PE"):
		p = p + 1
	if(i == "MG"):
		m = m + 1
	if(i == "SP"):
		s = s + 1
	if(i == "RS"):
		r = r + 1
z = zeros(5, dtype = int)
z[0] = a
z[1] = p
z[2] = m
z[3] = s
z[4] = r
print(int(max(z)))

print(z)
		