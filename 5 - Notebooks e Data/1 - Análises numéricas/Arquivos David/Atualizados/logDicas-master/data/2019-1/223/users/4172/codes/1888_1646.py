from numpy import*



x= array(eval(input("")))
q=0
for i in range(size(x)):
	if x[i]<=50:
		q+=1
a = zeros(q, dtype=int)
print(q)
r = 0
for i in range(size(x)):
	if x[i]<=50:
		a+=i
print(a)
