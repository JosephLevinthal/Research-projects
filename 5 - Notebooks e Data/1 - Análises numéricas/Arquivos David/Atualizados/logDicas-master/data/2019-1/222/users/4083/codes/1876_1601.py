from numpy import*
v = array(eval(input("Tempo dos corredores: ")))

a = min(v)
h = 0
for i in range(size(v)):
	if(v[i] == a):
		h = i 
print(h)