from numpy import*
x = array(eval(input("peso: ")))
y = array(eval(input("altura: ")))
z = zeros(size(x), dtype=float)

for i in x:
	z[i] = 