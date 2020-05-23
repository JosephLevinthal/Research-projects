x = float(input())
k = int(input())

s = 0
c = 0
aux = 1

while(c < k):
	s = s + aux * (x ** c)
	
	if(aux == 1):
		aux = -1
	else:
		aux = 1
	
	c = c + 1

print(round(s, 7))