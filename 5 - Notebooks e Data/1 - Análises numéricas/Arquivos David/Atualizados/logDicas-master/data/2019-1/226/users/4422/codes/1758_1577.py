from numpy import*
a = float(input("ac: "))
vo = float(input("vo: "))
n = int(input("n: "))

v = zeros(n)
i = 0

while (i < n):
	d = ((a *(i**2))/2) + vo*i 
	v[i] = d
	i = i + 1
print(v)
	