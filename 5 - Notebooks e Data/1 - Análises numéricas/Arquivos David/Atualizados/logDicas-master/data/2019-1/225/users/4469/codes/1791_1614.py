from numpy import*

a = array(eval(input()), dtype = str)
b = array(eval(input()), dtype = int)

s = 0.0
i = 0
while(i < size(a)):
	if(a[i].upper() == "BANANA"):
		s = s + (0.97 * b[i])
	elif(a[i].upper() == "BIFE"):
		s = s + (2.95 * b[i])
	elif(a[i].upper() == "FEIJOADA"):
		s = s + (1.27 * b[i])
	elif(a[i].upper() == "OMELETE"):
		s = s + (1.04 * b[i])
	elif(a[i].upper() == "TOMATE"):
		s = s + (0.2 * b[i])
	
	i = i + 1

print(round(s, 2))