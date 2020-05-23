from numpy import*
from numpy.linalg import*
m = array(eval(input("digite uma matriz: ")))
linha = m.shape [0]
coluna = m.shape [1]
for i in range(linha):
	print(max(m[i,:]))
