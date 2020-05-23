from numpy import *
pw = array(eval(input("Digite a forca do jogador: ")))
g1 = 0

for i in pw:
	if(i%2 == 0):
		g1 = g1 + 1
vg1 = zeros(g1, dtype=int)
j=0
for i in range(len(pw)):
	if(pw[i] % 2 != 0):
		vg1 = vg1
		j=j
	else:
		vg1[j] = pw[i]
		j = j+1
print(vg1)			
		