from numpy import*
a = array(eval(input("tempo de chegada: ")))

b = max(a)
c = size(a)
t = 0
while(t < c):
	if( a[t] == b):
		i = t
		t = c
	t += 1
print(i)