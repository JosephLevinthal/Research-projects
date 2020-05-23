from numpy import*
a = array(eval(input("Tempo dos corredores: ")))
b = min(a)
c = size(a)
t = 0
while (t<c):
	if a[t]==b:
		i = t
		t = c
	t +=1
print(i)
	