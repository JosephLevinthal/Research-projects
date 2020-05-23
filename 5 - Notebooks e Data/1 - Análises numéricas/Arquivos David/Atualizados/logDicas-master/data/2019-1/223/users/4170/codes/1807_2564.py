from numpy import*
golsA = array(eval(input("Numero de gols do time A: ")))
golsB = array(eval(input("Numero de gols do time B: ")))
x = zeros(3,dtype=int)
for i in range(size(golsA)):
	if(golsA[i] > golsB[i]):
		x[0] = x[0] + 1
	elif(golsA[i] == golsB[i]):
		x[1] = x[1] + 1
	elif(golsA[i] < golsB[i]):
		x[2] = x[2] + 1
print(x)		