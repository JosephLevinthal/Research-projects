x = 0
n = []

while(x >= 0):
	x = int(input())
	if(x >= 0):
		n.append(x)

c = 0
while(c < len(n)):
	expoente = len(str(n[c]))
	s = 0
	x1 = n[c]

	while(x1 != 0):
		s = s + ((x1 % 10) ** expoente)
		x1 = x1 // 10

	if(s == n[c]):
		print("ARMSTRONG")
	else:
		print("NAO ARMSTRONG")
		
	c = c + 1