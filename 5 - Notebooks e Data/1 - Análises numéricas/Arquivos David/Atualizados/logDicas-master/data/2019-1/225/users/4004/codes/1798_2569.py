from numpy import*
x = array(eval(input("vetores: ")))

d = 0
m = sum(x)/size(x)

for i in x:
	d = d + (((i - m) ** 2)/(size(x) - 1))
d = d ** 0.5
print(round(d, 3))