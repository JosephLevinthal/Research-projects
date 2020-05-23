from numpy import*

a = array(eval(input("digite: ")))
n = 0
for i in range(size(a)):
	if a[i] % 5 == 0:
		n = n + 1
	
new = zeros(n, dtype=int)

x = 0
y = 0

for i in range(size(a)):
	if a[i] % 5 == 0:
		new[x] = new[x] + i
		x = x +1
print(n)	
print(new)
	