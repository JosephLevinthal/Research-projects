from numpy import*
num = input("Numeros: ")
i = 0
d = 3
o = "."
s = ""
while(i<len(num)):
	if(i<(len(num)-4)):
		s = s + num[i:d] + o
	else:
		s = s + num[i:d]
	i = i + 3
	d = d + 3			 
print(s)