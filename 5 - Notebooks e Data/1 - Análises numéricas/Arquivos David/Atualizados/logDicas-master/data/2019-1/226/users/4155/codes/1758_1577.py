from numpy import *
a = float(input("a: "))
vo = float(input("vo: "))
n = int(input("n: "))
t = n - 1
i = 0
t = arange(n)
d = zeros(n)
while(i<size(t)):
	d[i] = ((a * (t[i] ** 2))/2) + vo * t[i]
	i = i + 1
print(d)