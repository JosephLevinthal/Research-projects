from numpy import*
x = array(eval(input("x: ")))
c = 1
m = sum(x)/size(x)
for y in x:
	c = c * abs(y - m)
p = c**(1/size(x))
print(round(p, 3))