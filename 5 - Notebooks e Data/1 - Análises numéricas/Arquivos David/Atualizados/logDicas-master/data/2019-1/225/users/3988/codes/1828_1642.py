from numpy import*
v = array(eval(input("entrada: ")))
s = 0
for i in v:
	if(i%5==0):
		s = s + 1
r = zeros(s,dtype=int)
print(s)
n = 0
for i in range(size(v)):
	
	if(v[i]%5==0):
		r[n]= i
		n = n + 1
print(r)
		



 
	
	