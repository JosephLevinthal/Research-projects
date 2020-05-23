from numpy import*
n = array(eval(input("vetor: ")))
x = sum(n)/size(n)
s = 0
for i in range(size(n)):
	s = s + (n[i] - x)**2
d = sqrt(s/ (size(n) - 1))
print(round(d, 3))