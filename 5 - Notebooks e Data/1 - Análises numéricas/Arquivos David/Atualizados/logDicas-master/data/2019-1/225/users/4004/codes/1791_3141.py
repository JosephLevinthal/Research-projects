from numpy import*

n = array(eval(input("Vetores de entrada: ")))

i = 0
s = size(n)
r = 0
while i < s:
	r = r + (n[i] ** (1/6))
	i = i + 1
m = (r/s) ** 6
print(round(m, 2))