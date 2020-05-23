from numpy import*
a = array(eval(input("Notas: ")))
i= 0 
for y in range(a):
	if (a[y]>= 5.0):
		i+=1
print(i)
#indicies
b = zeros(n,dtype=int)
c = 0 
d = 0
for y in 