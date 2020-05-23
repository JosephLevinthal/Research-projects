from numpy import*
# Definicado quadro de medalhas
quadro = array([
[46, 37, 38],
[27, 23, 17],
[26, 18, 26],
[19, 18, 19],
[17, 10, 15],
[12,  8, 21],
[10, 18, 14]
])
# Tipos de medalhas(no. de colunas)
MEDALHAS = shape(quadro)[1]
# Variavel acumuladora
total = 0
# Processa a j-esima coluna na linha 4
for j in range(MEDALHAS):
	total = total + quadro[6,j]
print(total)
