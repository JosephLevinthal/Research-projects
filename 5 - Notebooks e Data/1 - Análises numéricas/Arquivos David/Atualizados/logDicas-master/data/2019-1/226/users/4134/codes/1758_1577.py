from  numpy import*
a = float(input("ac:"))
v0 = float(input("vel:"))
num = int(input("num: "))

i = 0 
t = arange(num)
d = zeros(num)

while (i<size(t)):
	d[i] = a*t[i]**2/2. + v0 * t[i]
	i = i+1
print(d)