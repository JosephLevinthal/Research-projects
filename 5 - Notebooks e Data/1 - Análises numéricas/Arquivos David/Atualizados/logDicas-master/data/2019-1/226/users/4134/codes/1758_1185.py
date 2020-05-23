from numpy import*
a = array(eval(input("vai que e tua:")))

t=0
m=0
while (t<size(a)):
	if (a[t]>99):
		print(t)
		t= t+1
		m = m+1
	else:
		t = t+1
print(m)