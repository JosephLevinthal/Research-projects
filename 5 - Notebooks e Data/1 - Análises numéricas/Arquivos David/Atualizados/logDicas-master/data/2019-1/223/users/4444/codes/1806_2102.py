from numpy import *
# Definicao do quadro de medalhas
quadro = array([
[46, 37, 38],
[27, 23, 17],
[26, 18, 26],
[19, 18, 19],
[17, 10, 15],
[12,  8, 21],
[10, 18, 14]
])

# No. de paises (no. de linhas)
PAISES   = shape(quadro)[1]
# Variavel acumuladora
ouro = 0
# Percorre a i-esima linha na coluna 0
for i in range(PAISES):
	ouro = ouro + quadro[i,1]
print(ouro)