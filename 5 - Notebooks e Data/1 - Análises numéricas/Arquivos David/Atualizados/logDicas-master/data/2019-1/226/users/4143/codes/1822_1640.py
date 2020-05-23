from numpy import*
a = array(eval(input("Turmas :")))
#b = zeros(n,dtype=int)
i = 0
impar=0
sala=0
b = size(a)
for x in range(size(a)) :
	if (x[i]//2 !=0 ):
		sala+=1
	i+=1
print(sala)
c=0
j=0

for y in a:
	if (y[c]%2 !=0):
		y[c]=n[c]
		c+=1	
	j+=1
	
