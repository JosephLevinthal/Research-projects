N = int(input("numero se termos"))
H = 0
o = 1
for i in range(1,N):
	k = (1/o)
	if(i % 2 == 1):
		k = 1/o * (-1)
	elif(i % 2 == 0):
		k = (1/o)
	H = H - k
	o = o + 1
print(H)