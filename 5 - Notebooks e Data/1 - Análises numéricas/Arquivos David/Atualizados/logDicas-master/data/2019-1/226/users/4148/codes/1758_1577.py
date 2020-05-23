from numpy import*
a = float(input("vetor 1: "))
b = float(input("vetor 2: "))
n = int(input("n: "))

i = 0
t = arange(n)
d = zeros(n)



while(i<size(t)):
	d[i] = a * t[i]**2 / 2 + b * t[i]
	i = i + 1
	
print(d)