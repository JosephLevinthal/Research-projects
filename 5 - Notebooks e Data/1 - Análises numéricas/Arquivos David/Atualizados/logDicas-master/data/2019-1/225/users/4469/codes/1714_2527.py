x = int(input())

c = 1
s = 0

while(c < x):
	if(x % c == 0):
		print(c)
		s = s + c
	
	c = c + 1

if(s == x):
	print("PERFEITO")
else:
	print("NAO PERFEITO")