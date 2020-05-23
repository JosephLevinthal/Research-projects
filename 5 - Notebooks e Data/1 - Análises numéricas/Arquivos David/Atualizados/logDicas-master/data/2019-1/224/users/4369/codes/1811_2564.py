from numpy import*
g1 = array(eval(input("Digite o numero de gols: ")))
g2 = array(eval(input("Digite o numero de gols do advers: ")))
c = zeros(3, dtype = int)
for i in range(size(g1)):
	if g1[i] > g2[i]:
		c[0] = c[0] + 1
	if g1[i] < g2[i]:
		c[2] = c[2] + 1
	if g1[i] == g2[i]:
		c[1] = c[1] + 1
print(c)