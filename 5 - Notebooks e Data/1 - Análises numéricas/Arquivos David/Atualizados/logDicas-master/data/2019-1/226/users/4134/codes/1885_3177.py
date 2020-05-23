from numpy import*
def vogais():
	
	i = 0
	j = 0
	k = 0
	l = 0
	n = 0
	y = 0
	x = str(input("Palavra:"))
	x = x.lower()
	for i in x:
		if(i == "a"):
			j = j+1
		elif(i == "e"):
			k= k+ 1
		elif(i == "i"):
			l = l + 1
		elif(i == "o"):
			n = n + 1
		elif(i == "u"):
			y = y + 1
	print("a:", j)
	print("e:", k)
	print("i:", l)
	print("o:", n)
	print("u:", y)
vogais()
		