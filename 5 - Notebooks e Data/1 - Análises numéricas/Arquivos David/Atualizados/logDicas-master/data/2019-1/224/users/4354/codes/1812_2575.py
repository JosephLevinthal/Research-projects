from numpy import *
v = array(eval(input("digite o vetor de preferencias: ")))
n = 0
t = 0
y = 0
for i in v:
	i = i.upper()
	if(i == "NETFLIX"):
		n = n + 1
	if(i == "TV"):
		t = t + 1
	if(i == "YOUTUBE"):
		y = y + 1
z = zeros(3,dtype = int)
z[0] = t
z[1] = n
z[2] = y
print(z)
