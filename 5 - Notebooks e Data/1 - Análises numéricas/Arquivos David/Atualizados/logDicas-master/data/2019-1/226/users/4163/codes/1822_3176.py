x = input("digite: ").upper()

c = 0 
v = 0
for i in range(len(x)):
	if (x[i]== "A" or x[i]== "E" or x[i]== "I" or x[i]== "O" or x[i]== "U"):
		v = v + 1
	else:
		c = c + 1
		
print(v)
print(c)
		