from numpy import *
from numpy.linalg import *
# Definicao do quadro de medalhas
quadro = array([
[46, 37, 38],
[27, 23, 17],
[26, 18, 26],
[19, 18, 19],
[17, 10, 15],
[12, 8, 21],
[10, 18, 14]
])
x=quadro[:,1]
y=quadro[:,2]
w=quadro[2,:]
print(x,y,w)
soma=sum(quadro[:,1])
print(soma)