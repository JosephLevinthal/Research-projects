from numpy import*

nm = array(eval(input("n de matriculas:")))

impar = 0 
for i in range(0,size(nm)):
	if(nm[i] % 2 == 1 ):
		impar = impar + 1
		
g2 = zeros(impar, dtype=int)
a = 0
for i in range(0,size(nm)):
	if(nm[i] % 2 == 1):
		if(a < size(g2)):
			g2[a] = nm[i]
			a = a + 1
print(g2)