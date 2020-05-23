from numpy import*
g = array(eval(input("numero de gols: ")))
ga = array(eval(input("gols do time adversario: ")))
j = zeros(3, dtype=int)
i = 0

while (i < size(g)):
	if (g[i] > ga[i]):
		j[0] = j[0] + 1
		
	elif (g[i] == ga[i]):
		j[1] = j[1] + 1
		
	elif (g[i] < ga[i]):
		j[2] = j[2] + 1
	
	i = i + 1
print(j)
		
		


		

		