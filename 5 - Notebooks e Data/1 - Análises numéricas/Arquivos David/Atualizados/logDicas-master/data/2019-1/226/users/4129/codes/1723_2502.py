n = int(input("Numero de termos:"))

a = 0
b = 12**(1/2) 
c = 1
d = 0
s = 2
m = 0
while(a < n):
	pi = b * ((1/(c*3**d)) * (-1)**(s) + m)
	m =  (1/(c*3**d)) * (-1)**(s) + m
	c = c + 2
	d = d + 1
	a = a + 1
	s = s + 1
print(round(pi, 8))
	
	
	