from numpy import*
a = array(eval(input()))
m = sum(a)/size(a)
d = 1

for x in a:
	d *= abs(x-m)
	p = d**(1/size(a))
print(round(p,3))
	
	
	
	