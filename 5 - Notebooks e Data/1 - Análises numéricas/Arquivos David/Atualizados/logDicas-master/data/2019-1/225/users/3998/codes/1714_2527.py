k = int(input())
u = 0
v = 1
while(v < k):
	if(k % v == 0 ):
		u = u + v
		print(v)
	v = v + 1
if(k== u):
	print("PERFEITO")
else:
	print("NAO PERFEITO")