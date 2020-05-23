from numpy import*

v1 = array(eval(input("v1: ")))
v2 = array(eval(input("v2: ")))
i = 0
a = 0
b = 0
c = 0
d = 0
print(size(v1))

while	(size(v1) != i):
		if	(v1[i] == v2[i]):
			a = a + 1
		elif	(v1[i] == 11 and v2[i] == 22 ):
				b = b + 1
		elif	(v1[i] == 11 and v2[i] == 33):
				c = c + 1
		elif	(v1[i] ==  22 and v2[i] == 11):
				c = c + 1
		elif	(v1[i] ==  22 and  v2[i] == 33):
				b = b + 1
		elif	(v1[i] == 33 and  v2[i] == 11):
				b = b + 1
		elif	(v1[i] == 33 and v2[i]  == 22):
				c = c + 1
		
			
		i = i + 1
		
if	(b == c):
	 print("EMPATE")
		
elif	(c > b):
		print("EUSAPIA")
		
else:
	print("BARSANULFO")