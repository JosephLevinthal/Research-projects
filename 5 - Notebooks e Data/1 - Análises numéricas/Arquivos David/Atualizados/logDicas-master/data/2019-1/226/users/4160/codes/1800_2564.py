from numpy import*
v1 = array(eval(input("O numero de gols: ")))
v2 = array(eval(input("O numero de gols do time adversario: ")))

v3 = zeros(3,dtype=int)
# v[0] = vitorias
# v[1] = empates
# v[2] = derrotas
for i in range(size(v1)):
	if v1[i] > v2[i]:
		v3[0]= v3[0] + 1
	elif v1[i]==v2[i] :
		v3[1] = v3[1] + 1
	elif v1[i] < v2[i]:
		v3[2] = v3[2] + 1
print(v3)
		
		
		