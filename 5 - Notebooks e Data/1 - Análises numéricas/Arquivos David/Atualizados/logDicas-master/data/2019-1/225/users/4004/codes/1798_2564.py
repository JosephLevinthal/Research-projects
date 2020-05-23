from numpy import*

x = array(eval(input("numero de gols do time: ")))
y = array(eval(input("numero de gols do adversario: ")))
z = zeros(3, dtype=int) #vetor Estatistica

j = 0 #indice y

for i in x:
	if i > y[j]:
		z[0] = z[0] + 1
		j = j + 1
	elif i == y[j]:
		z[1] = z[1] + 1
		j = j + 1
	else:
		z[2] = z[2] + 1
		j = j + 1
print(z)