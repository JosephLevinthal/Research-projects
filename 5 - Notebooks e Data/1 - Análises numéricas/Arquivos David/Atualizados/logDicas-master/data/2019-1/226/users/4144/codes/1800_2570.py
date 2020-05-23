from numpy import *
x = array(eval(input("digite bro: ")))
m = sum(x)/size(x)
p = 1
h = size(x)
for i in range(size(x)):
	p = p * abs(x[i]-m)

print(round(p**(1/h),3))