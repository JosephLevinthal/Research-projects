from numpy import*
x = array(eval(input()))
m = sum(x)/size(x)
d = 0
for g in x:
	d += (g-m)**2
	w = d/(size(x)-1)
	q = sqrt(w)
	
print(round(q,3))