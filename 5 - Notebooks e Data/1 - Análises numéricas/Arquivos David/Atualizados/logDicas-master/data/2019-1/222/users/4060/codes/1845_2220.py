from numpy import *
from numpy.linalg import *
m_tabela=array(eval(input("valores: ")))
linha=shape(m_tabela)[0]
for i in range(linha):
	print(max(m_tabela[i,:]))#dar as saidas dos valores maximos