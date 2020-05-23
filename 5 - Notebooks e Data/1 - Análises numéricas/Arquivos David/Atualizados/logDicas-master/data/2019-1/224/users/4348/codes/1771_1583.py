from numpy import *
v = input("numero: ")
t = 0 
n = len(v)
a = ""
while (t<n):
	if (n):
		a=a + v[t]+v[t+1]+v[t+2]
		t = t +3
	else:
		a = a + v[t]+v[t+1]+v[t+2]
		t =t+3
print(a)
